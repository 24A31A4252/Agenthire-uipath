from pypdf import PdfReader

reader = PdfReader("resumes/sample_resume.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)