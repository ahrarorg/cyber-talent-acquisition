from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from .models import WorkRole, Candidate, JobPosting

app = FastAPI(title="Cyber Talent Acquisition API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data
work_roles = [
    WorkRole(
        id="OPM-711",
        name="Cyber Defense Analyst",
        description="Uses data collected from a variety of cyber defense tools...",
        tasks=["T0020", "T0023"],
        ksas=["K0001", "K0002"]
    ),
    WorkRole(
        id="OPM-621",
        name="Software Developer",
        description="Develops, creates, maintains, and writes computer applications...",
        tasks=["T0046", "T0171"],
        ksas=["K0003", "K0004"]
    )
]

job_postings = []
candidates = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cyber Talent Acquisition API"}

@app.get("/work-roles", response_model=List[WorkRole])
def get_work_roles():
    return work_roles

@app.post("/job-postings", response_model=JobPosting)
def create_job_posting(posting: JobPosting):
    posting.id = len(job_postings) + 1
    job_postings.append(posting)
    return posting

@app.get("/job-postings", response_model=List[JobPosting])
def get_job_postings():
    return job_postings

@app.post("/candidates", response_model=Candidate)
def register_candidate(candidate: Candidate):
    candidate.id = len(candidates) + 1
    candidates.append(candidate)
    return candidate

@app.get("/candidates", response_model=List[Candidate])
def get_candidates():
    return candidates
