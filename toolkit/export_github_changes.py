"""Emit a bounded batch of changed UTF-8 source files for an authorized API upload.

No credential handling, network access or external writes. Binary artifacts are separate.
"""
from pathlib import Path
import subprocess,json,sys
ROOT=Path(__file__).resolve().parents[1]
def run(*args):return subprocess.check_output(['git',*args],cwd=ROOT).decode().splitlines()
paths=sorted(set(run('diff','--name-only','HEAD')+run('ls-files','--others','--exclude-standard')))
allowed=('book/','toolkit/','tests/','docs/','output/pdf/')
paths=[p for p in paths if (p.startswith(allowed) or p=='README.md') and not p.endswith(('.png','.jpg','.pdf','.zip'))]
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
limit=int(sys.argv[2]) if len(sys.argv)>2 else 10
entries=[]
for p in paths[start:start+limit]:
 f=ROOT/p
 if not f.exists():entries.append(dict(path=p,mode='100644',type='blob',sha=None))
 else:entries.append(dict(path=p,mode='100644',type='blob',content=f.read_text(encoding='utf-8')))
print(json.dumps(dict(total=len(paths),next=start+len(entries),entries=entries)))
