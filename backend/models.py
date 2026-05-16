from pydantic import BaseModel
from typing import List, Optional

class KSA(BaseModel):
    id: str
    description: str
    type: str

class Task(BaseModel):
    id: str
    description: str

class WorkRole(BaseModel):
    id: str
    name: str
    description: str
    tasks: List[str] = []
    ksas: List[str] = []

class Candidate(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    applied_role_id: str
    skills_assessment: List[dict] = []

class JobPosting(BaseModel):
    id: Optional[int] = None
    title: str
    work_role_id: str
    description: str
    requirements: List[str] = []
