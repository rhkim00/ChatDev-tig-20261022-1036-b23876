def find_change_in_government_spending(Y, M_s, G, C, I):
    # Given equations
    C = 100 + 0.6 * Y
    I = 0.2 * Y - 50
    M_D = 0.25 * Y - 30
    M_s = 65
    
    print("Equations:")
    print("C =", C)
    print("I =", I)
    print("M_D =", M_D)
    print("M_s =", M_s)
    
    # Equilibrium condition
    Y = C + I + G
    
    print("\nEquilibrium condition:")
    print("Y =", Y)
    
    # Find the change in government spending required to close the deflationary gap
    def find_change_in_government_spending(Y, M_s, G, C, I):
        # Full employment level of income
        Y_full_employment = 600
        
        # Desired change
        desired_change = Y_full_employment - Y
        
        # Find the change in government spending required to close the deflationary gap
        change_in_government_spending = desired_change - (0.6 * desired_change)
        
        return change_in_government_spending
    
    result = find_change_in_government_spending(Y, M_s, G, C, I)
    
    print("\nFull employment level of income:", Y_full_employment)
    print("Desired change:", desired_change)
    print("Change in government spending required to close the deflationary gap:", result)
    
    return result

# Given values
Y = 500
M_s = 65
G = 100

# Find the change in government spending required to close the deflationary gap
change_in_government_spending = find_change_in_government_spending(Y, M_s, G, 100, 0.2 * Y - 50)

print("\nThe change in government spending required to close the deflationary gap is:", change_in_government_spending)