from services.career_db import CAREER_DB

# Each question maps to a set of skills/tags.
QUESTION_SKILL_MAP = [
    ["data analysis", "critical thinking", "problem solving"],                # Q1
    ["technical", "learning", "adaptability"],                               # Q2
    ["learning", "adaptability", "motivation"],                              # Q3
    ["leadership", "teamwork", "communication"],                             # Q4
    ["stress management", "resilience", "time management"],                  # Q5
    ["teamwork", "collaboration", "communication"],                          # Q6
    ["work environment", "organization", "flexibility"],                     # Q7
    ["motivation", "innovation", "stability"],                               # Q8
    ["creativity", "strategy", "innovation"],                                # Q9
    ["problem solving", "analytical", "systems thinking"],                   # Q10
    ["adaptability", "ambiguity", "decision making"],                        # Q11
    ["communication", "visual communication", "written communication"],      # Q12
    ["decision making", "research", "intuition"],                            # Q13
    ["risk taking", "initiative", "entrepreneurship"],                       # Q14
    ["decision making", "experience", "time management"],                    # Q15
]

# Assign weights to rare/critical skills (customize for your domain)
SKILL_WEIGHTS = {
    # Example: critical skills get higher weight
    "system design": 5,
    "machine learning": 5,
    "leadership": 3,
    "data analysis": 4,
    "communication": 3,
    # Default weight for any unspecified skill
}

def get_skill_weight(skill):
    return SKILL_WEIGHTS.get(skill, 1)

def quiz_answers_to_traits(answers: dict) -> set:
    """
    Convert quiz answers to a set of user traits/skills.
    Assumes answers are indexed as question number (0-based).
    """
    tags = set()
    for idx, val in answers.items():
        # "2" means strong agreement, maps to skills for that question
        if int(val) == 2 and int(idx) < len(QUESTION_SKILL_MAP):
            tags.update(QUESTION_SKILL_MAP[int(idx)])
    return tags

def weighted_match_score(user_traits: set, required_skills: set) -> int:
    """
    Calculate a weighted match score (0-100) between user traits and required skills.
    """
    overlap = user_traits & required_skills
    match_score = sum(get_skill_weight(skill) for skill in overlap)
    max_score = sum(get_skill_weight(skill) for skill in required_skills)
    if max_score == 0:
        return 0
    return round(match_score / max_score * 100)

def confidence_score(user_traits: set, required_skills: set) -> float:
    """
    Confidence (0.0-1.0): proportion of required skills matched.
    """
    overlap = user_traits & required_skills
    return round(len(overlap) / max(1, len(required_skills)), 2)

def explain_match(user_traits: set, career: dict) -> str:
    """
    Return human-readable explanation for why the user matches this career.
    """
    overlap = user_traits & set(career["required_skills"])
    missing = set(career["required_skills"]) - user_traits
    explanation = (
        f"You match '{career['name']}' because you possess: {', '.join(overlap) if overlap else 'no key skills'}.\n"
        f"To improve, focus on: {', '.join(missing) if missing else 'no missing skills'}."
    )
    return explanation

def predict_careers(quiz_data: dict):
    """
    Main prediction entry point. Returns top 5 career matches with scores, explanations, missing skills, and resources.
    """
    user_traits = quiz_answers_to_traits(quiz_data)
    results = []
    for career in CAREER_DB:
        required = set(career["required_skills"])
        match = weighted_match_score(user_traits, required)
        confidence = confidence_score(user_traits, required)
        missing_skills = list(required - user_traits)
        resources = career.get("resources", [])[:2]
        explanation = explain_match(user_traits, career)
        results.append({
            "title": career["name"],
            "description": career["description"],
            "match": match,
            "confidence": confidence,
            "skills": missing_skills,
            "resources": resources,
            "explanation": explanation,
        })
    # Sort by match score, highest first
    results = sorted(results, key=lambda r: r["match"], reverse=True)
    return results[:5]

# For compatibility with the rest of your backend, you may want to add:
def predict_career(quiz_data: dict):
    """
    Drop-in replacement for legacy code (returns tuple for DB model).
    """
    careers = predict_careers(quiz_data)
    recommended_roles = [r["title"] for r in careers]
    confidence_scores = {r["title"]: r["confidence"] for r in careers}
    model_used = "weighted-v2.0"
    return recommended_roles, confidence_scores, model_used

def analyze_skill_gaps(quiz_data: dict, career_name: str):
    """
    For storing skill gaps per prediction (for DB).
    """
    user_traits = quiz_answers_to_traits(quiz_data)
    career = next((c for c in CAREER_DB if c["name"] == career_name), None)
    if not career:
        return [], []
    missing_skills = list(set(career["required_skills"]) - user_traits)
    resources = career.get("resources", [])[:2]
    return missing_skills, resources