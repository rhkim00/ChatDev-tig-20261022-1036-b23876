import math

# Define the current wealth and the loss
current_wealth = 20000
loss = 10000

print("Current wealth: ", current_wealth)
print("Loss: ", loss)

# Define the utility function (logarithmic utility)
def utility(wealth):
    return math.log(wealth)

# Calculate the utility without insurance
utility_without_insurance = utility(current_wealth - loss)
print("Utility without insurance: ", utility_without_insurance)

# Calculate the utility with full insurance
utility_with_insurance = utility(current_wealth)
print("Utility with full insurance: ", utility_with_insurance)

# The correct answer is the utility with full insurance
correct_answer = round(utility_with_insurance, 3)
print("Correct answer: ", correct_answer)