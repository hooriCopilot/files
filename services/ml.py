from services.career_db import CAREER_DB

QUESTION_SKILL_MAP = [
    # Q1: Data analysis and critical thinking
    ["data analysis", "critical thinking", "problem solving"],

    # Q2: Technical aptitude and learning
    ["technical", "learning", "adaptability"],

    # Q3: Learning new skills and adaptability
    ["learning", "adaptability", "motivation"],

    # Q4: Leadership and teamwork
    ["leadership", "teamwork", "communication"],

    # Q5: Stress management, resilience, and time management
    ["stress management", "resilience", "time management"],

    # Q6: Teamwork and collaboration
    ["teamwork", "collaboration", "communication"],

    # Q7: Work environment preference (structure, flexibility)
    ["work environment", "organization", "flexibility"],

    # Q8: Motivation (innovation, stability, challenge)
    ["motivation", "innovation", "stability"],

    # Q9: Creativity and strategic thinking
    ["creativity", "strategy", "innovation"],

    # Q10: Problem solving (analytical, systems thinking)
    ["problem solving", "analytical", "systems thinking"],

    # Q11: Adaptability, ambiguity, and decision making
    ["adaptability", "ambiguity", "decision making"],

    # Q12: Communication style (verbal, written, visual)
    ["communication", "visual communication", "written communication"],

    # Q13: Decision making (research, intuition, data-driven)
    ["decision making", "research", "intuition"],

    # Q14: Risk-taking and initiative
    ["risk taking", "initiative", "entrepreneurship"],

    # Q15: Decision making speed and experience
    ["decision making", "experience", "time management"],
]
def quiz_answers_to_traits(answers: dict) -> set:
    tags = set()
    for idx, val in answers.items():
        if int(val) == 2:
            tags.update(QUESTION_SKILL_MAP[int(idx)])
    return tags

def predict_careers(quiz_data: dict):
    user_traits = quiz_answers_to_traits(quiz_data)
    results = []
    for career in CAREER_DB:
        required = set(career["required_skills"])
        overlap = user_traits & required
        match_score = round(len(overlap)/max(1,len(required)) * 100)
        missing_skills = list(required - user_traits)
        resources = career.get("resources", [])[:2]
        results.append({
            "title": career["name"],
            "description": career["description"],
            "match": match_score,
            "skills": missing_skills,
            "resources": resources
        })
    results = sorted(results, key=lambda r: r["match"], reverse=True)
    return results[:5]