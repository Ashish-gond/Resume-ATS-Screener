import re


SKILL_GROUPS = {
    "Java": ["java"],
    "Python": ["python"],
    "SQL": ["sql"],
    "MySQL": ["mysql"],
    "Git/GitHub": ["git", "github"],
    "Data Structures": ["data structures", "data structure"],
    "Algorithms": ["algorithms", "algorithm"],
    "OOP": [
        "oop",
        "object oriented programming",
        "object-oriented programming"
    ],
    "DBMS": [
        "dbms",
        "database management system"
    ],
    "Java Collections": [
        "java collections",
        "collections"
    ],
    "Exception Handling": [
        "exception handling"
    ],
    "Problem Solving": [
        "problem solving",
        "problem-solving"
    ]
}


def normalize_text(text):
    text = text.lower()
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text)
    return text


def analyze_skills(resume_text, job_description):

    resume = normalize_text(resume_text)
    job = normalize_text(job_description)

    matching_skills = []
    missing_skills = []

    for skill, keywords in SKILL_GROUPS.items():

        # Check whether this skill is required in the job description
        required = any(keyword in job for keyword in keywords)

        if not required:
            continue

        # Check whether this skill exists in the resume
        found = any(keyword in resume for keyword in keywords)

        if found:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matching_skills, missing_skills


def calculate_ats_score(resume_text, job_description):

    matching_skills, missing_skills = analyze_skills(
        resume_text,
        job_description
    )

    total_required = len(matching_skills) + len(missing_skills)

    if total_required == 0:
        return 0

    score = (len(matching_skills) / total_required) * 100

    return round(score, 2)