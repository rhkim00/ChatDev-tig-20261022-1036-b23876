data = {
    "question": "_______ theory can be described as a code of conduct to which all rational beings should adhere. This contrasts with ________ morality which is the code of conduct adopted by a particular group or society.",
    "answer_choices": {
        "A": "Normative, Ethical",
        "B": "Ethical, Descriptive",
        "C": "Normative, Instrumental",
        "D": "Normative, Descriptive",
        "E": "Descriptive, Ethical",
        "F": "Ethical, Normative",
        "G": "Instrumental, Normative",
        "H": "Descriptive, Normative",
        "I": "Normative, Prescriptive",
        "J": "Descriptive, Prescriptive"
    },
    "correct_answer": "F"
}

print("Question:")
print(data["question"])

print("\nAnswer Choices:")
for key, value in data["answer_choices"].items():
    print(f"{key}: {value}")

print("\nCorrect Answer:")
print(data["correct_answer"])