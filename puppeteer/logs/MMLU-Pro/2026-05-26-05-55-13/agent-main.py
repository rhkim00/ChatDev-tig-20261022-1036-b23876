def is_acid_anhydride(compound):
    # Define the list of acid anhydrides
    acid_anhydrides = ["CO2", "SO2", "SO3", "P2O5", "P4O10", "N2O5", "Cl2O7", "F2O", "H2S2O7"]
    
    # Convert the compound to its chemical formula
    formula = ""
    for char in compound:
        if char.isupper():
            formula += char
        else:
            formula += char.upper()
    
    print(f"Converted formula of {compound}: {formula}")
    
    # Check if the compound is an acid anhydride
    result = formula in acid_anhydrides
    print(f"Is {compound} an acid anhydride? {result}")
    
    return result

# Test the function
compounds = ["H2SO3", "NaCl", "CH4", "HNO3", "SO2", "Al(NO3)3", "CaCO3", "H2O", "HCl"]
for compound in compounds:
    is_acid_anhydride(compound)