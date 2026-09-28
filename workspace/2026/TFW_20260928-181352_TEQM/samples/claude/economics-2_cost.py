import json,sys
P={"claude-fable-5-1":dict(i=10,o=50,r=0.25),"claude-opus-5-5":dict(i=4,o=20,r=0.20),"claude-sonnet-5":dict(i=2,o=10,r=0.20)}
d=json.load(open(sys.argv[1],encoding="utf-8"))
tot={}; 
def cost(m,c):
    p=P[m]; return (c["input"]*p["i"]+c["cw5m"]*p["i"]*1.25+c["cw1h"]*p["i"]*2+c["cread"]*p["r"]+c["output"]*p["o"])/1e6
def parts(m,c):
    p=P[m]; return dict(input=c["input"]*p["i"]/1e6,cw=(c["cw5m"]*1.25+c["cw1h"]*2)*p["i"]/1e6,cread=c["cread"]*p["r"]/1e6,output=c["output"]*p["o"]/1e6)
for lab,v in d.items():
    grp="MEASURE" if lab.startswith("MEASURE") else "ROBBIE"
    for m,c in v["per_model"].items():
        x=cost(m,c); pr=parts(m,c)
        print(f"{lab:45s} {m:18s} calls={c['calls']:4d} in={c['input']:>7,} cw5m={c['cw5m']:>10,} cw1h={c['cw1h']:>9,} cread={c['cread']:>12,} out={c['output']:>9,} think={c['thinking']:>8,}  ${x:8.2f}  [in {pr['input']:.2f} cw {pr['cw']:.2f} cr {pr['cread']:.2f} out {pr['output']:.2f}]")
        t=tot.setdefault(grp,{"calls":0,"input":0,"cw5m":0,"cw1h":0,"cread":0,"output":0,"thinking":0,"usd":0.0})
        for k in ("calls","input","cw5m","cw1h","cread","output","thinking"): t[k]+=c[k]
        t["usd"]+=x
for g,t in tot.items():
    allin=t["input"]+t["cw5m"]+t["cw1h"]+t["cread"]
    print(g, {k:(round(v,2) if isinstance(v,float) else f"{v:,}") for k,v in t.items()}, "input-side total", f"{allin:,}", "grand", f"{allin+t['output']:,}")
