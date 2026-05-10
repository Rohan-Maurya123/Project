SKILLS = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "nlp",
    "deep learning",
    "power bi",
    "excel"
]

def extract_skills(text):

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills