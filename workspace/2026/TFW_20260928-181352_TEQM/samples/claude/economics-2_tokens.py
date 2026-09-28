import json, glob, os, collections, datetime as dt
base = r"C:\Users\c0rpa\.claude\projects\E--projects-kids-friendly-ai"
label={"24b16148-68a5-4483-a9ed-de7703088aaa.jsonl":"MEASURE (this session, README задача из TFW)",
 "4ef441df-2766-4845-9456-1d6a63638d85.jsonl":"PLAN · ROBBIE (coordinator, main thread)",
 r"4ef441df-2766-4845-9456-1d6a63638d85\subagents\agent-adb0478c58f827410.jsonl":"researcher-robbie",
 r"4ef441df-2766-4845-9456-1d6a63638d85\subagents\agent-a7e389d39ef7f5d57.jsonl":"reviewer-robbie",
 r"4ef441df-2766-4845-9456-1d6a63638d85\subagents\agent-a53c7153c7e53dee1.jsonl":"executor-robbie"}
F=["input","cw5m","cw1h","cread","output","thinking","ws","wf"]
def ts(s): return dt.datetime.fromisoformat(s.replace("Z","+00:00"))
out={}
for rel,lab in label.items():
    f=os.path.join(base,rel)
    best={}; stamps=[]; sids=set(); agentlaunch=[]
    for line in open(f,encoding="utf-8"):
        try: d=json.loads(line)
        except: continue
        if d.get("timestamp"): stamps.append(ts(d["timestamp"]))
        if d.get("sessionId"): sids.add(d["sessionId"])
        r=d.get("toolUseResult")
        if isinstance(r,dict) and "agentId" in r: agentlaunch.append((r.get("agentId"),r.get("status")))
        m=d.get("message") if isinstance(d.get("message"),dict) else None
        if d.get("type")!="assistant" or not m or "usage" not in m: continue
        u=m["usage"]; cc=u.get("cache_creation") or {}; st=u.get("server_tool_use") or {}; od=u.get("output_tokens_details") or {}
        rec=dict(model=m.get("model"),input=u.get("input_tokens",0),cw5m=cc.get("ephemeral_5m_input_tokens",0),cw1h=cc.get("ephemeral_1h_input_tokens",0),
                 cwtot=u.get("cache_creation_input_tokens",0),cread=u.get("cache_read_input_tokens",0),output=u.get("output_tokens",0),
                 thinking=od.get("thinking_tokens",0),ws=st.get("web_search_requests",0),wf=st.get("web_fetch_requests",0),t=ts(d["timestamp"]))
        k=m["id"]
        if k not in best or rec["output"]>=best[k]["output"]:
            if k in best: rec["thinking"]=max(rec["thinking"],best[k]["thinking"])
            best[k]=rec
    stamps.sort()
    active=sum(((b-a).total_seconds() for a,b in zip(stamps,stamps[1:]) if (b-a).total_seconds()<=300),0.0)
    per=collections.defaultdict(lambda: collections.Counter())
    mism=0
    for r in best.values():
        c=per[r["model"]]; c["calls"]+=1
        for x in F: c[x]+=r[x]
        if r["cwtot"]!=r["cw5m"]+r["cw1h"]: mism+=1
    out[lab]=dict(file=rel,sessionIds=sorted(sids),first=stamps[0].isoformat(),last=stamps[-1].isoformat(),
        span_h=round((stamps[-1]-stamps[0]).total_seconds()/3600,2),active_h_gap5m=round(active/3600,2),
        cw_split_mismatch=mism,agent_results=agentlaunch,per_model={k:dict(v) for k,v in per.items()})
print(json.dumps(out,indent=1,ensure_ascii=False))
