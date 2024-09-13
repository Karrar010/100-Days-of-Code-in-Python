#Task 1
# seperate 2 digit numbers
print("The Seperator")
num = str(input("2 Digit Number: "))
print("Seperated Form: ",num[0]," + ",num[1]," = ",int(num[0])+int(num[1])) #since a string is a sequence of chars

#Task 2
# BMI Calculator
print("--BMI CALC--")
kg = float(input("Enter Weight (Kg) : "))
meters = float(input("Enter Height (m2) : "))
BMI = kg/(meters)**2
print("Your BMI is : ",int(BMI))

#Tas 3
#Days,Weeks,Months Calculator
print(" --Time Left of this Earth-- ")
age = int(input("Your Age: "))
years = 90 - age
months = years*12
weeks = years*52
Days = years*365
print(f"You have {Days} days, {weeks} weeks and {months} months Left.")