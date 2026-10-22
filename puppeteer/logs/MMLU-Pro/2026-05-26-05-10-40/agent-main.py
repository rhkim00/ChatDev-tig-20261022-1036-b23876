import math

def calculate_light_gathering_ratio():
    # Given values
    eye_diameter_mm = 5
    telescope_aperture_cm = 50

    # Convert diameter from mm to cm
    eye_diameter_cm = eye_diameter_mm / 10
    print("Eye diameter in cm:", eye_diameter_cm)

    # Calculate the ratio of the telescope aperture to the eye diameter
    ratio = (telescope_aperture_cm / eye_diameter_cm) ** 2
    print("Light gathering ratio:", ratio)

    return ratio

ratio = calculate_light_gathering_ratio()
print("The telescope can gather", ratio, "times more light than the eye.")