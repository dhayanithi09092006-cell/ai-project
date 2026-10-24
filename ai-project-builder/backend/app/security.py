from fastapi import HTTPException
SKIP={"node_modules",".git","__pycache__",".venv","venv","dist","build",".next",".cache"}
def safe_path(p):
 if not isinstance(p,str) or not p or len(p)>240: raise HTTPException(400,"Invalid path")
 p=p.replace("\\\\","/")
 parts=p.split("/")
 if p.startswith("/") or any(x in ("",".","..") for x in parts): raise HTTPException(400,"Unsafe path")
 if any(x.lower() in SKIP for x in parts): raise HTTPException(400,"Dependency/build path forbidden")
 if any(x==".env" or (x.startswith(".env.") and x!=".env.example") for x in parts): raise HTTPException(400,"Environment file forbidden")
 if parts[-1].lower() in {"credentials.json","secrets.json","id_rsa"}: raise HTTPException(400,"Credential file forbidden")
 return p
def safe_files(d):
 if not isinstance(d,dict) or not d or len(d)>100: raise HTTPException(502,"Invalid AI file map")
 out={}; size=0
 for p,c in d.items():
  p=safe_path(p)
  if not isinstance(c,str): raise HTTPException(502,"File content must be text")
  size+=len(c.encode())
  if size>2000000: raise HTTPException(502,"Project too large")
  out[p]=c
 return out
def include(p):
 parts=p.split("/")
 return not any(x.lower() in SKIP for x in parts) and parts[-1].lower() not in {"credentials.json","secrets.json","id_rsa",".env"} and not (parts[-1].startswith(".env.") and parts[-1]!=".env.example")
