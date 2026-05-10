from src.main_pipeline import process_resumes

with open("data/sample_jd.txt", "r") as file:
    jd = file.read()

results = process_resumes("resumes", jd)

results.to_csv("outputs/ranking_report.csv", index=False)

print(results)