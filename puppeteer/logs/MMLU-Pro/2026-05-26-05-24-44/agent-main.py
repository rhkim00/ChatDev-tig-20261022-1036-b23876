data = {
    'question': '_______ is the direct attempt to formally or informally manage ethical issues or problems, through specific policies, practices and programmes.',
    'options': {
        'A': 'Operational management',
        'B': 'Corporate governance',
        'C': 'Environmental management',
        'D': 'Business ethics management',
        'E': 'Sustainability',
        'F': 'Stakeholder management',
        'G': 'Social marketing',
        'H': 'Human resource management'
    },
    'correct_answer': 'D: Business ethics management'
}

print("Question: ", data['question'])
print("\nOptions:")
for key, value in data['options'].items():
    print(f"{key}: {value}")

print("\nCorrect Answer: ", data['correct_answer'])