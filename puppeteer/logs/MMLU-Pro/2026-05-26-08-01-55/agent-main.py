import json

def solve_business_pricing_strategy():
    """
    This function solves the business pricing strategy question.

    Returns:
        A dictionary containing the answer and explanation.
    """
    question = "Where the price is set low relative to the competition to gain market share, this strategy is known as:" 
    options = {
        "A": "Captive product pricing.",
        "B": "High-low pricing.",
        "C": "Price skimming.",
        "D": "Value added pricing.",
        "E": "Penetration pricing.",
        "F": "Premium pricing.",
        "G": "Cost-plus pricing.",
        "H": "Economy pricing.",
        "I": "Psychological pricing.",
        "J": "Competitive pricing."
    }
    answer = "E: Penetration pricing."

    result = {
        "question": question,
        "options": options,
        "answer": answer
    }

    return result

# Run the function and print the result in JSON format
result = solve_business_pricing_strategy()
print("Question:", result["question"])
print("Options:")
for key, value in result["options"].items():
    print(f"{key}: {value}")
print("Answer:", result["answer"])
print("\nResult in JSON format:")
print(json.dumps(result, indent=4))