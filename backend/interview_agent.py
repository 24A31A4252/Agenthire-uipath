candidate_skills = [
    "Python",
    "Machine Learning",
    "Git",
    "GitHub",
    "Data Analysis"
]

questions = {
    "Python": [
        "What are Python decorators?",
        "Difference between list and tuple?"
    ],
    "Machine Learning": [
        "What is overfitting?",
        "Explain supervised learning."
    ],
    "Git": [
        "What is a merge conflict?",
        "Explain git rebase."
    ],
    "GitHub": [
        "Difference between Git and GitHub?"
    ],
    "Data Analysis": [
        "How do you handle missing values in a dataset?"
    ]
}

print("\n=== Interview Questions ===\n")

for skill in candidate_skills:
    if skill in questions:
        print(f"\n{skill}:")
        for q in questions[skill]:
            print("-", q)