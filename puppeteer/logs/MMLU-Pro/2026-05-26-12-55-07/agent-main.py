def get_answer():
    # Define the options
    options = {
        "A": "equitably manage the sales bonus pool",
        "B": "increase the competitiveness within the sales team",
        "C": "create multiple points of contact between the customer and the company",
        "D": "distribute the work involved in managing an account",
        "E": "reduce the workload of individual salespeople",
        "F": "ensure that every team member gets to interact with the customer",
        "G": "diversify the company's customer base",
        "H": "match various functional areas of the company with customer needs",
        "I": "simplify the process of sales negotiation",
        "J": "provide a single point of contact for the customer with the company"
    }

    # Define the correct answer
    correct_answer = "J"

    # Print the options
    print("The primary objective of team-based selling is to:")
    for key, value in options.items():
        print(f"{key}. {value}")

    # Ask the user for their answer
    user_answer = input("Enter your answer (A-J): ")

    # Check if the user's answer is correct
    if user_answer.upper() == correct_answer:
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

get_answer()