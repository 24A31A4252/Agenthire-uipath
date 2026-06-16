import json

candidate_name = "Varun Pakkurthi"

found_skills = [
    "Python",
    "Java",
    "C",
    "JavaScript",
    "React",
    "Git",
    "GitHub",
    "Machine Learning",
    "Data Analysis"
]

match_score = 71.43
recommendation = "Recommended"

report = {
    "candidate_name": candidate_name,
    "skills": found_skills,
    "match_score": match_score,
    "recommendation": recommendation
}

with open("outputs/report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Report saved successfully!")