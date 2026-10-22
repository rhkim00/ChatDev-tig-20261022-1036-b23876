# Define the percentages as decimal values
percent1 = 0.65 / 100
percent2 = 0.42 / 100

# Print the values of percent1 and percent2
print(f"Percent1: {percent1*100}%")
print(f"Percent2: {percent2*100}%")

# Calculate the percentage of percent1 that is equal to percent2
result = (percent2 / percent1) * 100

# Print the result
print(f"The percentage of {percent1*100}% that is {percent2*100}% is {result}%")