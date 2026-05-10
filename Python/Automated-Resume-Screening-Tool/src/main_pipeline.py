import os
import pandas as pd

from src.extractors.pdf_extractor import extract_text_from_pdf
from src.extractors.docx_extractor import extract_text_from_docx

from src.preprocessing.cleaner import clean_text

from src.matching.skill_matcher import extract_skills
from src.matching.scorer import calculate_similarity


def process_resumes(resume_folder, job_description):

    results = []

    for root, dirs, files in os.walk(resume_folder):

        for file in files:

            file_path = os.path.join(root, file)

            text = ""

            try:

                if file.endswith(".pdf"):
                    text = extract_text_from_pdf(file_path)

                elif file.endswith(".docx"):
                    text = extract_text_from_docx(file_path)

                else:
                    continue

                cleaned_text = clean_text(text)

                # Skip empty resumes
                if len(cleaned_text.strip()) < 20:
                    print(f"Skipped empty/unreadable resume: {file}")
                    continue

                skills = extract_skills(cleaned_text)

                score = calculate_similarity(
                    job_description,
                    cleaned_text
                )

                decision = (
                    "Shortlisted"
                    if score >= 35
                    else "Rejected"
                )

                category = os.path.basename(root)

                results.append({
                    "Resume": file,
                    "Actual Category": category,
                    "Skills": ", ".join(skills),
                    "Score": score,
                    "Decision": decision
                })

            except Exception as e:

                print(f"Error processing {file}: {e}")

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="Score",
        ascending=False
    )

    return df