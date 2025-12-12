from typing import List, Dict

JOB_CATALOG = [
    {"id":1, "title":"Junior Software Engineer", "seniority":"Junior", "skills":["python","git","data-structures"]},
    {"id":2, "title":"Software Engineer", "seniority":"Mid", "skills":["python","git","system-design","sql"]},
    {"id":3, "title":"Senior Software Engineer", "seniority":"Senior", "skills":["python","system-design","aws","leadership"]},
    {"id":4, "title":"Data Analyst", "seniority":"Junior", "skills":["sql","excel","data-visualization"]},
    {"id":5, "title":"Data Scientist", "seniority":"Mid", "skills":["python","ml","sql","statistics"]},
    {"id":6, "title":"Engineering Manager", "seniority":"Manager", "skills":["leadership","hiring","system-design"]}
]

SENIORITY_ORDER = {"Junior":0, "Mid":1, "Senior":2, "Lead":3, "Manager":4}


def score_role_for_user(user_skills:List[str], current_role_seniority:str, candidate_role:Dict) -> float:
    overlap = len(set(s.lower() for s in user_skills).intersection(s.lower() for s in candidate_role["skills"]))
    skill_score = overlap / max(1, len(candidate_role["skills"]))

    cur = SENIORITY_ORDER.get(current_role_seniority, 0)
    cand = SENIORITY_ORDER.get(candidate_role["seniority"], 0)
    seniority_score = 1.0 - abs(cand - cur) * 0.2
    seniority_score = max(0, seniority_score)

    return 0.7 * skill_score + 0.3 * seniority_score


def suggest_next_roles(user_skills:List[str], current_seniority:str, top_k:int=3):
    scored = []
    for job in JOB_CATALOG:
        sc = score_role_for_user(user_skills, current_seniority, job)
        scored.append((job, sc))

    scored.sort(key=lambda x: x[1], reverse=True)

    results = []
    for job, sc in scored[:top_k]:
        missing_skills = [s for s in job["skills"] if s.lower() not in [u.lower() for u in user_skills]]
        results.append({
            "title": job["title"],
            "seniority": job["seniority"],
            "score": round(sc, 3),
            "missing_skills": missing_skills
        })

    return results