# backend/app/main.py
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# -----------------------------
# APP INIT
# -----------------------------
app = FastAPI(title="Career Trajectory Engine")

# Allow React frontend to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# STATIC FILES (React build)
# -----------------------------
static_path = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_path):
    raise RuntimeError(f"Static folder not found at {static_path}. Please build your frontend first.")

app.mount("/static", StaticFiles(directory=static_path), name="static")

# Serve React index.html for root path
@app.get("/")
def serve_frontend():
    index_file = os.path.join(static_path, "index.html")
    return FileResponse(index_file)

# -----------------------------
# API MODELS
# -----------------------------
class ProfileInput(BaseModel):
    current_title: str
    current_seniority: str
    skills: List[str]
    years_experience: int

# -----------------------------
# API ENDPOINT
# -----------------------------
@app.post("/profile")
def profile(input: ProfileInput):
    # Placeholder logic — replace with your ML model or processing
    suggestion = f"Based on your title '{input.current_title}' and skills {input.skills}, we suggest aiming for next seniority level in 2 years."
    return {"suggestion": suggestion}

# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.get("/health")
def health_check():
    return {"message": "FastAPI backend is working!"}
