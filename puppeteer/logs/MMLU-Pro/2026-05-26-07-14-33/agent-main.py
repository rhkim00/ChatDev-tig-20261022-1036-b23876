import random
options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
num_choices = 1000
choices = [random.choice(options) for _ in range(num_choices)]
print("Generated choices:", choices)

frequency = {}
for choice in choices:
    if choice in frequency:
        frequency[choice] += 1
    else:
        frequency[choice] = 1

print("Frequency of each choice:", frequency)

most_common = max(frequency, key=frequency.get)
print("Most common choice:", most_common)