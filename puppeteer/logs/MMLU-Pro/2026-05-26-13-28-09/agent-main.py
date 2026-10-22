base_bodily_injury_premium = 101
base_property_damage_premium = 48
bodily_injury_factor = 1.37
property_damage_factor = 1.10
bodily_injury_coverage = (25/50) * base_bodily_injury_premium * bodily_injury_factor
property_damage_coverage = (25/50) * base_property_damage_premium * property_damage_factor

print("Base Bodily Injury Premium: $", base_bodily_injury_premium)
print("Base Property Damage Premium: $", base_property_damage_premium)
print("Bodily Injury Factor: ", bodily_injury_factor)
print("Property Damage Factor: ", property_damage_factor)

print("Bodily Injury Coverage: $", round(bodily_injury_coverage, 2))
print("Property Damage Coverage: $", round(property_damage_coverage, 2))