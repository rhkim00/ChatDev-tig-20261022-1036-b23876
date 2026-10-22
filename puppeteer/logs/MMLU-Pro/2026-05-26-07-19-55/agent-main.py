import json

def psychology_question():
    # Define the question and options
    question = "According to Caplan's model of consultee-centered case consultation, the consultant is primarily interested in"
    options = {
        "A": "identifying the causes and solutions of the client's presenting problems",
        "B": "establishing a hierarchy of authority to enable effective decision making",
        "C": "ensuring the consultee adheres strictly to a predetermined action plan",
        "D": "proposing multiple alternative solutions for the consultee to choose from",
        "E": "identifying the strengths and weaknesses of the consultee's current approach",
        "F": "presenting a single, well-defined and unambiguous course of action for the consultant to overcome skills deficits",
        "G": "developing a comprehensive treatment plan for the client",
        "H": "identifying and eliminating the causes of the consultee's difficulties in handling a problem",
        "I": "focusing on the consultant's personal growth and development",
        "J": "focusing on the relationship between the client and the consultee"
    }

    # Define the correct answer
    correct_answer = "E"

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
        print(key + ":", value)

    # Print the correct answer
    print("Correct Answer:", correct_answer)

    # Print the result in JSON format
    print("Result:", json.dumps(result))

# Run the function
psychology_question()