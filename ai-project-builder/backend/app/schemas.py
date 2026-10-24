from pydantic import BaseModel,Field
class Spec(BaseModel):
 topic:str=Field(min_length=10,max_length=12000)
 stack:str=Field(default="Python + FastAPI + PyTorch",max_length=300)
class Generate(Spec):
 project_name:str=Field(default="medical-image-federated-learning",min_length=1,max_length=80)
class RepoCreate(BaseModel):
 name:str=Field(min_length=1,max_length=100,pattern=r"^[A-Za-z0-9._-]+$")
 description:str=Field(default="",max_length=350)
 private:bool=False
class Publish(BaseModel):
 project_id:str
 repo_full_name:str=Field(min_length=3,max_length=200)
 branch:str=Field(default="main",min_length=1,max_length=100)
 message:str=Field(default="Publish generated project",max_length=200)
 confirmation_token:str=Field(min_length=20,max_length=200)
