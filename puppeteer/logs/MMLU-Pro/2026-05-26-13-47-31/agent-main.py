data = {"options": {"A": "Feedback", "B": "Message formulation", "C": "Channel", "D": "Transmission", "E": "Reception", "F": "Transfer", "G": "Encoding", "H": "Interpretation", "I": "Noise", "J": "Decoding"}, "correct_answer": "G"}

# Print the options
print("Options:")
for key, value in data["options"].items():
    print(f"{key}: {value}")

# Print the correct answer
print("Correct Answer:")
print(data["correct_answer"])