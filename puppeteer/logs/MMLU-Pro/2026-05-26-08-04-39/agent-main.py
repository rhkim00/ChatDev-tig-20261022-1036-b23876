data = {
    "question": "Once a train pulls out of a station, or an aeroplane takes off or a film starts, those seats are lost and can never be sold. This is referred to as:",
    "options": {
        "A": "Immeasurability",
        "B": "Impalpability",
        "C": "Variability",
        "D": "Non-storability",
        "E": "Indivisibility",
        "F": "Perishability",
        "G": "Non-recoverability",
        "H": "Inseparability",
        "I": "Heterogeneity",
        "J": "Intangibility"
    },
    "correct_answer": "F"
}

print("Question:", data["question"])
print("Options:")
for key, value in data["options"].items():
    print(key + ":", value)
print("Correct Answer:", data["correct_answer"])