import json

def solve_business_question():
    # Define the question and options
    question = "As what is ensuring that one individual does not carry the burden of a whole work task referred to?"
    options = {
        "A": "Work delegation",
        "B": "Workload balancing",
        "C": "Work distribution",
        "D": "Work specialisation",
        "E": "Work rotation",
        "F": "Work redundancy",
        "G": "Work shift",
        "H": "Work division",
        "I": "Work schedule",
        "J": "Work design"
    }

    # Define the correct answer
    correct_answer = "Work delegation"

    # Create a dictionary to store the result
    result = {
        "question": question,
        "options": options,
        "correct_answer": correct_answer
    }

    # Print the question
    print("Question:", question)

    # Print the options
    print("Options:")
    for key, value in options.items():
        print(f"{key}: {value}")

    # Print the correct answer
    print("Correct Answer:", correct_answer)

    # Print the result in JSON format
    print("Result in JSON format:")
    print(json.dumps(result, indent=4))

# Run the function
solve_business_question()