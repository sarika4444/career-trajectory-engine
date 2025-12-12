# backend/app/engine.py
from typing import List, Dict, Any
from collections import Counter

# -------------------------
# JOB CATALOG
# -------------------------
JOB_CATALOG = [
    {"id":1, "title":"Junior Software Engineer", "canonical":"SDE I", "seniority":"Junior",
     "skills":["python","git","data-structures"]},

    {"id":2, "title":"Software Engineer", "canonical":"SDE II", "seniority":"Mid",
     "skills":["python","git","system-design","sql","rest apis"]},

    {"id":3, "title":"Senior Software Engineer", "canonical":"Senior SDE", "seniority":"Senior",
     "skills":["python","system-design","aws","leadership","docker"]},

    {"id":4, "title":"Associate Software Engineer", "canonical":"Associate SDE", "seniority":"Junior",
     "skills":["java","git","rest apis","sql"]},

    {"id":5, "title":"Engineering Manager", "canonical":"EM", "seniority":"Manager",
     "skills":["leadership","hiring","system-design","project management"]},

    {"id":6, "title":"Data Analyst", "canonical":"Data Analyst", "seniority":"Junior",
     "skills":["sql","excel","data-visualization"]},

    {"id":7, "title":"Data Scientist", "canonical":"Data Scientist", "seniority":"Mid",
     "skills":["python","ml","sql","statistics"]},

    {"id":8, "title":"ML Engineer", "canonical":"ML Engineer", "seniority":"Mid",
     "skills":["python","ml","tensorflow","deployments","aws"]},

    {"id":9, "title":"Product Manager", "canonical":"PM", "seniority":"Mid",
     "skills":["product sense","roadmapping","stakeholder management"]},

    {"id":10, "title":"Solutions Engineer", "canonical":"Solutions Engineer", "seniority":"Mid",
     "skills":["customer success","rest apis","demos","communication"]}
]

# -------------------------
# SALARY TABLE
# -------------------------
SALARY_RANGES = {
    "Junior Software Engineer": "₹3L - ₹6L",
    "Software Engineer": "₹6L - ₹12L",
    "Senior Software Engineer": "₹12L - ₹25L",
    "Associate Software Engineer": "₹4L - ₹8L",
    "Engineering Manager": "₹25L - ₹45L",
    "Data Analyst": "₹3L - ₹7L",
    "Data Scientist": "₹8L - ₹20L",
    "ML Engineer": "₹10L - ₹30L",
    "Product Manager": "₹12L - ₹40L",
    "Solutions Engineer": "₹6L - ₹15L"
}

# -------------------------
# CAREER TRACKS
# -------------------------
CAREER_TRACKS = {
    "Engineering": [
        "Junior Software Engineer",
        "Software Engineer",
        "Senior Software Engineer",
        "Engineering Manager"
    ],
    "Product": [
        "Software Engineer",
        "Solutions Engineer",
        "Product Manager"
    ],
    "ML": [
        "Data Analyst",
        "Data Scientist",
        "ML Engineer"
    ]
}

SENIORITY_ORDER = {"Junior":0, "Mid":1, "Senior":2, "Lead":3, "Manager":4}

# -------------------------
# HELPERS
# -------------------------
def _normalize(skills: List[str]) -> List[str]:
    return [s.strip().lower() for s in skills]


def score_role_for_user(user_skills: List[str], current_role_seniority: str, candidate_role: Dict) -> float:
    user_set = set(_normalize(user_skills))
    role_skills = set(_normalize(candidate_role["skills"]))

    overlap = len(user_set & role_skills)
    skill_score = overlap / max(1, len(role_skills))

    cur = SENIORITY_ORDER.get(current_role_seniority.capitalize(), 0)
    cand = SENIORITY_ORDER.get(candidate_role["seniority"].capitalize(), 0)

    seniority_score = max(0, 1.0 - abs(cand - cur) * 0.2)

    return 0.7 * skill_score + 0.3 * seniority_score


# -------------------------
# MAIN ENGINE OUTPUTS
# -------------------------
def suggest_next_roles(user_skills: List[str], current_seniority: str, top_k: int = 3) -> List[Dict[str,Any]]:
    scored = []

    for job in JOB_CATALOG:
        sc = score_role_for_user(user_skills, current_seniority, job)
        scored.append((job, sc))

    scored.sort(key=lambda x: x[1], reverse=True)

    results = []
    for job, sc in scored[:top_k]:
        missing_skills = [
            s for s in job["skills"]
            if s.lower() not in _normalize(user_skills)
        ]

        results.append({
            "title": job["title"],
            "canonical": job["canonical"],
            "seniority": job["seniority"],
            "score": round(sc, 3),
            "missing_skills": missing_skills,
            "salary_range": SALARY_RANGES.get(job["title"], "N/A")
        })

    return results


def skill_gap_for_role(user_skills: List[str], role_title: str) -> List[str]:
    user_set = set(_normalize(user_skills))

    target = next((j for j in JOB_CATALOG if j["title"].lower() == role_title.lower()), None)
    if not target:
        return []

    return [
        s for s in target["skills"]
        if s.lower() not in user_set
    ]


def get_career_tracks(title: str) -> Dict[str, List[str]]:
    tracks = {}

    for track_name, seq in CAREER_TRACKS.items():
        if title in seq or seq[0].split()[0].lower() in title.lower():
            tracks[track_name] = seq

    if not tracks:
        tracks = CAREER_TRACKS

    return tracks


def predict_salary(title: str) -> str:
    return SALARY_RANGES.get(title, "N/A")


def recommended_skills_from_suggestions(suggestions: List[Dict[str,Any]], top_n: int = 5) -> List[str]:
    missing = []
    for s in suggestions:
        missing.extend(s["missing_skills"])

    counted = Counter([m.lower() for m in missing])
    return [skill.capitalize() for skill, _ in counted.most_common(top_n)]
