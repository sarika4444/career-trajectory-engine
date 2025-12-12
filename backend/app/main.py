import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional

from app.engine import (
    suggest_next_roles,
    recommended_skills_from_suggestions,
    skill_gap_for_role,
    get_career_tracks,
    predict_salary
)

app = FastAPI(title="Career Trajectory Engine")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- static serving (safe, serve both /static and /assets) ---
from fastapi.staticfiles import StaticFiles
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")

# serve everything under /static (index.html + assets folder)
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    # also mount /assets -> static/assets so index.html that references /assets/... works
    assets_dir = os.path.join(STATIC_DIR, "assets")
    if os.path.exists(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

# Serving Vite build
BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Serve index.html for root
@app.get("/")
def serve_frontend():
    index_path = os.path.join(STATIC_DIR, "index.html")
    return FileResponse(index_path)


# ---------------- API -------------------

class ProfileIn(BaseModel):
    current_title: str
    current_seniority: str
    skills: List[str]
    years_experience: Optional[int] = 0
    target_role: Optional[str] = None

@app.post("/profile")
async def profile(p: ProfileIn):

    suggestions = suggest_next_roles(p.skills, p.current_seniority, top_k=5)

    top_role = p.target_role if p.target_role else (
        suggestions[0]["title"] if suggestions else None
    )

    skill_gap = skill_gap_for_role(p.skills, top_role) if top_role else []

    tracks = get_career_tracks(p.current_title)

    rec_skills = recommended_skills_from_suggestions(suggestions, top_n=6)

    salary_est = predict_salary(top_role) if top_role else "N/A"

    return JSONResponse({
        "suggestions": suggestions,
        "top_role": top_role,
        "skill_gap": skill_gap,
        "recommended_skills": rec_skills,
        "career_tracks": tracks,
        "salary_estimate_for_top_role": salary_est
    })


@app.get("/health")
def health():
    return {"status": "ok"}
