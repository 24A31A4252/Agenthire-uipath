from pypdf import PdfReader

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

reader = PdfReader("resumes/sample_resume.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text + "\n"

found_skills = []

for skill in skills_database:
    if skill.lower() in resume_text.lower():
        print(f"Matched: {skill}")
        found_skills.append(skill)

score = min(len(found_skills) * 10, 100)

print("\n=== Resume Analysis Report ===\n")

print("Skills Found:")
for skill in found_skills:
    print("-", skill)

print(f"\nCandidate Score: {score}/100")