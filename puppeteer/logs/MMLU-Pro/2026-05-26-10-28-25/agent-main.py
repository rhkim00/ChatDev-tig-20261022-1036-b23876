def get_culture_type():
    culture_types = {
        'A': 'Process culture',
        'B': 'Hierarchical culture',
        'C': 'Power culture',
        'D': 'Competitive culture',
        'E': 'Collaborative culture',
        'F': 'Individualistic culture',
        'G': 'Task culture'
    }

    characteristic = 'Workers\' acceptance of change'

    for key, value in culture_types.items():
        if characteristic in value:
            print(f"Culture type found: {value}")
            return key

    print("No matching culture type found.")
    return "Error"

print(get_culture_type())