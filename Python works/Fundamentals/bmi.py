#program to calculate bmi

#bmi=(weight_in_kg/height_in_meter square)

weight_in_kg=72
height_in_cm=165

height_in_meter=165/100
bmi=weight_in_kg/height_in_meter**2
print(f"bmi of a person with height {height_in_cm} and weight {weight_in_kg}={bmi}")