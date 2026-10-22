data = {
    "question": "An important characteristic of services is that they are produced and consumed by people, simultaneously, as a single event. One of the outcomes of this unique process is that it is exceedingly difficult to standardize the delivery of services around the blueprint model. Which characteristic of service is this referred to?",
    "options": {
        "A": "Incomparability",
        "B": "Inconsistency",
        "C": "Simultaneity",
        "D": "Heterogeneity",
        "E": "Inseparability",
        "F": "Non-storable",
        "G": "Intangibility",
        "H": "Perishability",
        "I": "Variability",
        "J": "Non-transferability"
    },
    "correct_answer": "E"
}

print("Question:", data["question"])
print("Options:")
for key, value in data["options"].items():
    print(key + ":", value)
print("Correct Answer:", data["options"][data["correct_answer"]])