def managerial_functions():
    # Define the managerial functions in the correct order
    functions = ['planning', 'organising', 'leading', 'controlling']
    
    # Print the correct order
    print("The correct order of managerial functions is: ", functions)
    
    # Define the options
    options = [
        ['planning', 'organising', 'leading', 'controlling'],
        ['controlling', 'organising', 'leading', 'planning'],
        ['organising', 'leading', 'planning', 'controlling'],
        ['organising', 'controlling', 'leading', 'planning'],
        ['leading', 'planning', 'organising', 'controlling'],
        ['planning', 'organising', 'leading', 'controlling'],
        ['controlling', 'planning', 'organising', 'leading'],
        ['organising', 'planning', 'controlling', 'leading'],
        ['planning', 'organising', 'controlling', 'leading'],
        ['leading', 'controlling', 'planning', 'organising']
    ]
    
    # Define the correct answer
    correct_answer = functions
    
    # Iterate over the options
    for i, option in enumerate(options):
        # Check if the option is correct
        if option == correct_answer:
            # Print the correct option
            print("The correct option is: ", i+1)
            break

# Run the function
managerial_functions()