from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import WorkRole, Operative, Mission

app = FastAPI(title="Cyber Talent Acquisition API - Hacker Recruitment")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NIST NICE Offensive Security Roles
work_roles = [
    WorkRole(
        id="OPM-541",
        name="Exploit Developer",
        description="Identifies, counteracts, and exploits vulnerabilities in systems...",
        tasks=["T0561", "T0562"],
        ksas=["K0001", "K0034"]
    ),
    WorkRole(
        id="OPM-511",
        name="Vulnerability Assessment Analyst",
        description="Performs assessments of systems and networks...",
        tasks=["T0028", "T0549"],
        ksas=["K0002", "K0005"]
    ),
    WorkRole(
        id="OPM-531",
        name="Red Team Operator",
        description="Simulates adversary tactics to identify weaknesses...",
        tasks=["T0550", "T0551"],
        ksas=["K0003", "K0624"]
    )
]

missions = []
operatives = []

@app.get("/")
def read_root():
    return {"message": "System Active. Recruitment Protocol Initialized."}

@app.get("/work-roles", response_model=List[WorkRole])
def get_work_roles():
    return work_roles

@app.post("/missions", response_model=Mission)
def create_mission(mission: Mission):
    mission.id = len(missions) + 1
    missions.append(mission)
    return mission

@app.get("/missions", response_model=List[Mission])
def get_missions():
    return missions

@app.post("/operatives", response_model=Operative)
def register_operative(operative: Operative):
    operative.id = len(operatives) + 1
    operatives.append(operative)
    return operative

@app.get("/operatives", response_model=List[Operative])
def get_operatives():
    return operatives
