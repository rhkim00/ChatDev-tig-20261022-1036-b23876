data = {
    "question": "______ are the obligations of workers towards their employer, based on individual contracts and wider employment laws.",
    "options": ["A: Employer obligations", "B: Employment laws", "C: Employer benefits", "D: Employer duties", "E: Employee rights", "F: Employer rights", "G: Employee duties", "H: Employee benefits", "I: Employee contracts"],
    "answer": "G: Employee duties"
}

print("Question: ", data["question"])
print("Options:")
for option in data["options"]:
    print(option)
print("Answer: ", data["answer"])