#BMI Calculator
print("--BMI CALCULATOR--")
kg = float(input("Enter Weight (Kg) : "))
meters = float(input("Enter Height (m2) : "))
BMI = kg/(meters)**2
bmi = int(BMI)
print("Your BMI is : ",int(BMI))
if bmi <18.5 and bmi>=10:
    print("You are underweight.")
elif bmi <=25 and bmi >=18.5:
    print('You have a Normal Weight')
elif bmi <=30 and bmi >25:
    print("You are OverWeight")
elif bmi <=35 and bmi>30:
    print("You are Obese")
else:
    print("Dude, Take care of your Body or else its Game over")