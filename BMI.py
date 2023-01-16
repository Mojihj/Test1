# calculate BMI
from cgi import print_arguments


height=float(input("Enter your height:"))
weight=float(input("Enter your weight:"))
bmi=(weight/(height**2))
print(bmi)
if bmi<18.5:
    print("BMI:",bmi,"Your Condition Is Underweight")
elif bmi>=18.5 and bmi<25:
    print("BMI:",bmi,"Your Condition Is Normal")
elif bmi>=25 and bmi<30:
    print("BMI:",bmi,"Your Condition Is Overweight")
else:
    print("BMI:",bmi,"Your Condition Is Obesity")
print ("The End Of Calculation")