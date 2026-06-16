from pypdf import PdfReader
import re

# Skills database
skills_database = [
    "Python",
    "Java",
    "C",
    "JavaScript",
    "React",
    "Git",
    "GitHub",
    "Machine Learning",
    "Data Analysis",
    "SQL",
    "Power BI"
]

# Read Resume PDF
reader = PdfReader("resumes/sample_resume.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text + "\n"

# Extract candidate skills
candidate_skills = []

for skill in skills_database:
    pattern = r"\b" + re.escape(skill) + r"\b"

    if re.search(pattern, resume_text, re.IGNORECASE):
        candidate_skills.append(skill)

# Read Job Description
with open("docs/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

job_skills = []

for skill in skills_database:
    pattern = r"\b" + re.escape(skill) + r"\b"

    if re.search(pattern, job_description, re.IGNORECASE):
        job_skills.append(skill)

# Calculate Match Score
matched = []

for skill in candidate_skills:
    if skill in job_skills:
        matched.append(skill)

score = (len(matched) / len(job_skills)) * 100

print("\n=== Candidate Matching Report ===\n")

print("Candidate Skills:")
print(candidate_skills)

print("\nJob Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched)

print(f"\nMatch Score: {score:.2f}%")

# Recommendation
if score >= 80:
    recommendation = "Strongly Recommended"
elif score >= 60:
    recommendation = "Recommended"
else:
    recommendation = "Needs Review"

print("\nRecommendation:", recommendation)