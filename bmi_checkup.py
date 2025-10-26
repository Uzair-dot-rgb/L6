height = float(input("Enter yout height in cm : "))
weight = float(input("Enter your weight in kg : "))

BMI = weight/ (height/100)**2

print("Your BMI is ",BMI)

if BMI <= 18.4 :
    print("You are underweight.")
elif BMI <= 24.9 :
    print("You are healthy.")
elif BMI <= 29.9 :
    print("You are overwieght.")
elif BMI <= 34.9 :
    print("You are severly overwieght")
elif BMI <= 39.9 :
    print("You are obese.")
else :
    print("You are severly overobese.")