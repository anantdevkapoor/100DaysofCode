weight=float(input("Please Enter your weight in Kilograms "))
height=float(input("Please Enter your Height in Meters "))
BMI=round(weight/(height*height),1)
if BMI>=35.0:
    print(f"You BMI is {BMI} and you are Clinically Obese")
elif BMI>=30.0:
    print(f"You BMI is {BMI} and you are Obese")
elif BMI>=25.0:
    print(f"You BMI is {BMI} and you are Overweight")
elif BMI>=18.5:
    print(f"You BMI is {BMI} and you are Normal Weight")
else:
    print(f"You BMI is {BMI} and you are Underweight")
