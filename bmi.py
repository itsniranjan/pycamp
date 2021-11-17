height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = (weight/((height)**2))
bmi_int = int(bmi)

print(f"Your BMI is {bmi_int}")
