def find_most_common(results):
    # Get the most common key in the results dictionary
    most_common_key = max(results, key=results.get)
    print("Most common key:", most_common_key)

    # Get the corresponding value
    value = results[most_common_key]
    print("Corresponding value:", value)

    # Find the most common word in the value
    words = value.split()
    most_common_word = max(set(words), key=words.count)
    print("Most common word in the value:", most_common_word)

    # Return the most common word
    return most_common_word

# Define the results dictionary
results = {"individualism": "Individualism and long-term orientation", "power_distance": "Individualism and power distance", "uncertainty_avoidance": "Uncertainty avoidance", "long_term_orientation": "Long-term orientation", "masculinity": "Individualism and masculinity"}

# Find the most common word
most_common_word = find_most_common(results)

# Print the most common word
print("Most common word overall:", most_common_word)