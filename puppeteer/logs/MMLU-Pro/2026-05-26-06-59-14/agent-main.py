terms = {'A': 'a weak conscious mind', 'B': 'a strong conscious mind', 'C': 'a weak id', 'D': 'a weak ego', 'E': 'a weak unconscious mind', 'F': 'a strong id', 'G': 'a strong ego', 'H': 'a strong superego', 'I': 'a strong preconscious mind', 'J': 'a weak superego'}
max_count = 0
max_term = ''

for term, description in terms.items():
    count = description.count('weak')
    print(f"Term: {term}, Description: {description}, Weak Count: {count}")
    if count > max_count:
        max_count = count
        max_term = term

print(f"\nTerm with the highest count of 'weak' is: {max_term}")