print(""" _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")
print("\n------>>> MY CALCULATOR <<<------\n")

def add(num1,num2):
    result = float(num1 + num2)
    print(f"The Result of Operation is: {result}")
    return result
def subtract(num1,num2):
    result = float(num1 - num2)
    print(f"The Result of Operation is: {result}")
    return result
def multiply(num1,num2):
    result = float(num1 * num2)
    print(f"The Result of Operation is: {result}")
    return result
def divide(num1,num2):
    result = float(num1 / num2)
    print(f"The Result of Operation is: {result}")
    return result

output = True
num1 = float(input("What is the first number? "))

while(output):
    opera = str(input("What is the Operation between operands? ( + , - , * , / )  "))
    num2 = float(input("What is the second number? "))

    if opera == "+":
        num1 = add(num1,num2)
    elif opera == "-":
        num1 = subtract(num1,num2)
    elif opera == "*":
        num1 = multiply(num1,num2)
    elif opera == '/':
        num1 = divide(num1,num2)
    else:
        print("ERROR101: Wrong operation Entered.")
        break

    choice = str(input("Do you want to continue the operations? yes(y) or no(n)  Ans: "))
    if choice == 'y':
        output = True
    else: 
        output = False