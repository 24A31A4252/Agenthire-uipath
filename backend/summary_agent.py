def generate_summary(skills, score):
    return f"""
Candidate demonstrates experience in {', '.join(skills[:5])}.
Match Score: {score}%.
Recommended for further evaluation.
"""