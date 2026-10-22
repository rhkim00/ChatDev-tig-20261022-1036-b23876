def get_culture_type():
    # Dictionary to store culture types and their characteristics
    culture_types = {
        'A': 'Process culture',
        'B': 'Hierarchical culture',
        'C': 'Power culture',
        'D': 'Competitive culture',
        'E': 'Individualistic culture',
        'F': 'Task culture',
        'G': 'Collaborative culture'
    }

    # Dictionary to store question and answer
    question_answer = {
        'question': 'Workers\' acceptance of change is characteristic of what type of culture?',
        'answer': 'G: Collaborative culture'
    }

    # Get the culture type based on the question and answer
    for key, value in culture_types.items():
        if value == question_answer['answer']:
            print(f"Culture Type: {value}")
            print(f"Key for the Culture Type: {key}")
            return key

    print("Culture Type: Unknown culture type")
    return 'Unknown culture type'

print("Result of get_culture_type():")
print(get_culture_type())