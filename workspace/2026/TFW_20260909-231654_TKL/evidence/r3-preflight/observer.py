"""Finite TKL byte observer. Preflight reads sealed archives only; tree/file modes need later authority."""
import argparse, datetime, hashlib, json, subprocess, zipfile
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
TASK = HERE.parent.parent
ROOT = TASK.parents[2]
POSITIVE_COMMIT = '6b0d5c748d51c55c7c22147799cdb70131c22049'
CHECKPOINT = '793cd97f71f484fcbe7c2e01dcfe7503148b402d'
RAW_COMMIT = '1a0a37c443fe0d762a1396f1354d93ac08391637'
ARCHIVE_SHA = '7ac460d99dbf9c39ca51d969ae03292d6652d2b6584c227fe2e8d45d795b2f42'
POSITIVE_SHA = 'f0377bc0d2bbc3f4a420b712733e8df042c1356535468139295f64635759c45c'

def observe_bytes(data):
    pairs = data.count(b'\r\n')
    return {'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
            'raw_git_blob':hashlib.sha1(b'blob '+str(len(data)).encode('ascii')+b'\0'+data).hexdigest(),
            'eol':{'CRLF':pairs, 'LF':data.count(b'\n')-pairs, 'CR':data.count(b'\r')-pairs}}

def safe_member(name):
    p=PurePosixPath(name)
    return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name

def write_json(path, value):
    Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')

def git_bytes(commit,path):
    return subprocess.check_output(['git','-c','core.longpaths=true','-c','core.autocrlf=false','show',commit+':'+path.relative_to(ROOT).as_posix()],cwd=ROOT)

def bound():
    assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime.fromisoformat('2026-09-13T21:59:18+00:00'),'preflight deadline'

def preflight():
    started=datetime.datetime.now(datetime.timezone.utc).isoformat(); bound()
    archive=TASK/'evidence/r2-native/06-partial-physical.zip'
    positive_path=TASK/'evidence/r1-ac7/14-repeat-before-map.json'
    feasibility_path=TASK/'evidence/r2-checkpoint/06-native-feasibility.json'
    archive_data=archive.read_bytes(); assert hashlib.sha256(archive_data).hexdigest()==ARCHIVE_SHA
    assert archive_data==git_bytes(RAW_COMMIT,archive)
    original=positive_path.read_bytes(); assert hashlib.sha256(original).hexdigest()==POSITIVE_SHA
    assert original==git_bytes(POSITIVE_COMMIT,positive_path)
    feasibility_bytes=feasibility_path.read_bytes(); assert feasibility_bytes==git_bytes(CHECKPOINT,feasibility_path)
    feasibility=json.loads(feasibility_bytes); positive=json.loads(original)
    expected={r['path']:r for r in feasibility['positive_repository_files']}
    assert len(expected)==2317
    assert feasibility['positive_map_sha256']==POSITIVE_SHA
    observed={}; failures=[]
    with zipfile.ZipFile(archive) as z:
        members=[x.filename for x in z.infolist() if not x.is_dir()]
        assert len(members)==len(set(members))==2317
        assert all(safe_member(x) for x in members)
        assert set(members)==set(expected)
        for name in sorted(members):
            data=z.read(name); actual=observe_bytes(data); observed[name]=actual
            accepted=positive[name]; feasible=expected[name]
            for field in ['bytes','sha256','raw_git_blob','eol']:
                if actual[field]!=accepted[field] or actual[field]!=feasible[field]:
                    failures.append({'path':name,'field':field,'actual':actual[field],'accepted':accepted[field],'feasibility':feasible[field]})
    witness=b'\x00A\r\nB\nC\rD\r\n\xffE\n\r'
    witness_observed=observe_bytes(witness)
    assert witness_observed['eol']=={'CRLF':2,'LF':2,'CR':2}
    witness_result={'hex':witness.hex(),'expected_eol_by_hand':{'CRLF':2,'LF':2,'CR':2},'actual':witness_observed,'meaning':'LF and CR exclude bytes consumed by CRLF; includes NUL and non-UTF8 byte'}
    write_json(HERE/'02-all-files.json',observed);write_json(HERE/'02-witness.json',witness_result)
    bound()
    result={'started_at':started,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'outcome':'PASS' if not failures else 'FAIL','checked_files':len(observed),'failures':failures,'archive':{'path':archive.relative_to(ROOT).as_posix(),'commit':RAW_COMMIT,'sha256':ARCHIVE_SHA},'positive_oracle':{'path':positive_path.relative_to(ROOT).as_posix(),'commit':POSITIVE_COMMIT,'sha256':POSITIVE_SHA},'feasibility':{'path':feasibility_path.relative_to(ROOT).as_posix(),'commit':CHECKPOINT,'sha256':hashlib.sha256(feasibility_bytes).hexdigest()},'observer':observe_bytes(Path(__file__).read_bytes()),'receiver_access':False,'extracted_archive_files':0,'output_files':['02-all-files.json','02-witness.json','02-result.json'],'meaning':'All 2317 archive members match original accepted positive epoch and feasibility in every byte identity and all three EOL counters. R2 partial EOL fields are not an oracle.'}
    write_json(HERE/'02-result.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ['archive','positive_oracle','feasibility']},ensure_ascii=False))
    assert not failures, 'archive comparison failed'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=['preflight','file','tree']);ap.add_argument('--root');ap.add_argument('--output');args=ap.parse_args()
    if args.mode=='preflight':
        assert args.root is None and args.output is None; preflight();return
    assert args.root and args.output
    target=Path(args.root).resolve();out=Path(args.output).resolve()
    # Observation modes are read-only with respect to the subject; no extraction, checkout or update exists here.
    assert out!=target and not out.is_relative_to(target), 'output must be outside observation subject'
    if args.mode=='file': result={target.name:observe_bytes(target.read_bytes())}
    else:
        result={}
        for path in sorted(target.rglob('*')):
            rel=path.relative_to(target)
            if '.git' in rel.parts:continue
            assert not path.is_symlink(),str(rel)
            if path.is_file():result[rel.as_posix()]=observe_bytes(path.read_bytes())
    write_json(out,result)
    print(json.dumps({'mode':args.mode,'files':len(result),'output':str(out),'observer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}))

if __name__=='__main__':main()
