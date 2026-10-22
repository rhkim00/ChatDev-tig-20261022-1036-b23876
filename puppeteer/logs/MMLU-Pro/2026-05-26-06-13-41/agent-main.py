data = {
    "options": {
        "A": "Email Trojans",
        "B": "Backdoor Trojans",
        "C": "Rootkit Trojans",
        "D": "Banking Trojans",
        "E": "Trojan-Downloader",
        "F": "Spyware Trojans",
        "G": "Network Trojans",
        "H": "Worm Trojans",
        "I": "Ransom Trojan",
        "J": "IM – Trojans"
    },
    "correct_answer": "C"
}

print("Options:")
for key, value in data["options"].items():
    print(f"{key}: {value}")

print("\nCorrect Answer:")
print(data["correct_answer"])