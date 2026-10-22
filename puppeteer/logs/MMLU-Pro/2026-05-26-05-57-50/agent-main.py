import math

def calculate_pka(pH, moles_acid, volume_liters):
    # Calculate the concentration of the acid in moles per liter
    concentration_acid = moles_acid / volume_liters
    print('Concentration of the acid:', concentration_acid)

    # Calculate the concentration of the conjugate base
    # Since the acid is monoprotic, the concentration of the conjugate base is equal to the concentration of the acid
    concentration_base = concentration_acid
    print('Concentration of the conjugate base:', concentration_base)

    # Calculate the pKa using the Henderson-Hasselbalch equation
    pka = pH - math.log10(concentration_base / concentration_acid)
    print('pKa calculated using Henderson-Hasselbalch equation:', pka)

    return pka

# Given values
pH = 3.89
moles_acid = 0.0050  # in moles
volume_liters = 0.500  # in liters

# Calculate the pKa
pka = calculate_pka(pH, moles_acid, volume_liters)

# Print the result
print('The pKa of the acid is:', pka)