def get_precedent():
    # Define the cases
    cases = {
        'A': 'Brown v. Board of Education',
        'B': 'Miranda v. Arizona',
        'C': 'Roe v. Wade',
        'D': 'Betts v. Brady',
        'E': 'Plessy v. Ferguson',
        'F': 'Dred Scott v. Sandford',
        'G': 'Weeks v. United States',
        'H': 'Gideon v. Wainwright',
        'I': 'Marbury v. Madison',
        'J': 'Mapp v. Ohio'
    }

    # Define the correct answer
    correct_answer = 'Miranda v. Arizona'

    # Find the correct answer
    for key, value in cases.items():
        if value == correct_answer:
            print(f"Found correct answer: {value}")
            print(f"Key for correct answer: {key}")
            return key

    # If no match is found, return "Error"
    print("No match found for the correct answer.")
    return "Error"

print("Calling get_precedent():")
print(get_precedent())