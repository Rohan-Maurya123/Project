from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.matching.skill_matcher import extract_skills

def calculate_similarity(job_description, resume_text):
    if not job_description.strip() or not resume_text.strip():
        return 0.0

    try:
        # 1. TF-IDF Cosine Similarity (Semantic match)
        documents = [job_description.lower(), resume_text.lower()]
        tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", stop_words='english')
        matrix = tfidf.fit_transform(documents)
        
        if matrix.shape[1] == 0:
            semantic_score = 0.0
        else:
            similarity_score = cosine_similarity(matrix[0:1], matrix[1:2])
            semantic_score = float(similarity_score[0][0])

        # 2. Skill-based matching (Keyword match)
        jd_skills = set(extract_skills(job_description))
        resume_skills = set(extract_skills(resume_text))
        
        if not jd_skills:
            # If no specific skills in JD, rely entirely on semantic score
            final_score = semantic_score
        else:
            skill_match_count = len(jd_skills.intersection(resume_skills))
            skill_score = skill_match_count / len(jd_skills)
            
            # Weighted average: 20% Semantic, 80% Skill Match
            final_score = (semantic_score * 0.2) + (skill_score * 0.8)
            
            # Significant Boost for high skill match
            if skill_score >= 0.7:
                final_score = min(1.0, final_score + 0.4) # Increased from 0.3
            elif skill_score >= 0.4:
                final_score = min(1.0, final_score + 0.3) # Increased from 0.2
            elif skill_score > 0:
                final_score = min(1.0, final_score + 0.2) # Increased from 0.1

        # Scale to 100 and round
        result_score = round(final_score * 100, 2)
        return result_score
        
    except Exception as e:
        return 0.0