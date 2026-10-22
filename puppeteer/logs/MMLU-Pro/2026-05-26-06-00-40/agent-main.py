import math

# Given values
moles_acetic_acid = 2.00
moles_calcium_acetate = 1.00
pKa_acetic_acid = 4.76

# Calculate the ratio of [A-] to [HA]
ratio = moles_calcium_acetate / moles_acetic_acid
print('The ratio of [A-] to [HA] is:', ratio)

# Calculate the pH of the solution
pH = pKa_acetic_acid + math.log10(ratio)
print('The pH of the solution is:', pH)

# Calculate the buffer capacity of the solution
buffer_capacity = 0.5  # mole/L

# Calculate the number of moles of nitric acid that can be added before the pH begins to change significantly
moles_HNO3 = buffer_capacity * (moles_acetic_acid + moles_calcium_acetate)
print('The number of moles of nitric acid that can be added before the pH begins to change significantly is:', moles_HNO3)