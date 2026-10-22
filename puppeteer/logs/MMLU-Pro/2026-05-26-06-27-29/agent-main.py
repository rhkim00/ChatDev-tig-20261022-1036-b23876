import math

# Given values
num_turns = 100
length = 0.04  # in meters
width = 0.03   # in meters
control_torque = 240 * 10**-6  # in N-m
magnetic_flux_density = 1  # in Wb/m^2

print("Given values:")
print("Number of turns:", num_turns)
print("Length:", length, "m")
print("Width:", width, "m")
print("Control torque:", control_torque, "N-m")
print("Magnetic flux density:", magnetic_flux_density, "Wb/m^2")

# Calculate range
range_meters = (control_torque * num_turns) / (length * width * magnetic_flux_density)

print("\nCalculated range in meters:", range_meters, "m")

# Convert range to milliamps (assuming 1 A = 1 V and 1 V = 1 mA)
range_milliamps = range_meters / (length * width * magnetic_flux_density) * 1000

print("Range converted to milliamps:", range_milliamps, "mA")