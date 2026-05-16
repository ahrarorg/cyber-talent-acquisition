from pydantic import BaseModel
from typing import List, Optional

class KSA(BaseModel):
    id: str
    description: str
    type: str # Knowledge, Skill, or Ability

class Task(BaseModel):
    id: str
    description: str

class WorkRole(BaseModel):
    id: str
    name: str
    description: str
    tasks: List[str] = []
    ksas: List[str] = []

class Operative(BaseModel):
    id: Optional[int] = None
    alias: str
    email: str
    assigned_mission_id: Optional[str] = None
    competency_profile: List[dict] = [] # List of {ksa_id: score}

class Mission(BaseModel):
    id: Optional[int] = None
    codename: str
    work_role_id: str
    objective: str
    requirements: List[str] = []
