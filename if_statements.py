height = 1.8
weight = 65
bmi = weight / height ** 2

print(f"BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal Weight")
elif bmi >= 25 and bmi <= 29.9:  # 25 <= bmi <= 29.9
    print("Overweight")
else:
    print("Obese")

if 10 == 10.00:
    print("Equal")
else:
    print("Not Equal")

sentence = "Kenya, Uganda and Tanzania"

if "kenya" in sentence.lower():
    print("Yes, it exists")
else:
    print("Does not exists")

