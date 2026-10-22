def find_number_of_workers():
    # Define the supply curve equation
    def supply_curve(w):
        return 80 * w

    # Define the labor demand curve equation
    def labor_demand_curve(w):
        return 400 - 40 * w

    # Find the hourly wage where the supply curve and labor demand curve intersect
    w = (400 / 80)
    print('Hourly wage where supply curve and labor demand curve intersect:', w)

    # Find the number of workers that Carl will hire
    l = supply_curve(w)
    print('Number of workers that Carl will hire using supply curve equation:', l)

    # Find the number of workers that Carl will hire using the labor demand curve equation
    l_demand = 400 - 40 * w
    print('Number of workers that Carl will hire using labor demand curve equation:', l_demand)

    # Check if the number of workers from both equations are equal
    if round(l) == round(l_demand):
        print('Number of workers hired:', round(l))
        return round(l)
    else:
        return 'No intersection found'

# Run the function and print the result
result = find_number_of_workers()
print('The final answer is', result)