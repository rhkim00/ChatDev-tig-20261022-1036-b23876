data = {
    "question": "These objectives are often the most suitable when firms operate in a market dominated by a major competitor and where their financial resources are limited.",
    "options": {
        "A": "Hold objectives",
        "B": "Expansion objectives",
        "C": "Market objectives",
        "D": "Competitive objectives",
        "E": "Niche objectives",
        "F": "Harvest objectives",
        "G": "Divest objectives",
        "H": "Growth objectives"
    },
    "correct_answer": "D"
}

print("Question: ", data["question"])
print("Options:")
for key, value in data["options"].items():
    print(key + ": " + value)
print("Correct Answer: ", data["correct_answer"])