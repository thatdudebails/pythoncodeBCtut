import time

number1 = int(input("What would you like your first number to be?:"))
number2 = int(input("What would you like your second number to be?:"))
function = input("What function would you like to use for this equation(+, -, *, /)?:")
answer = 0

if function == "+":
    print(str(number1), "+", str(number2), "=", number1 + number2)
    answer = number1 + number2

elif function == "-":
    print(str(number1), "-", str(number2), "=", number1 - number2)
    answer = number1 - number2

elif function == "*":
    print(str(number1), "*", str(number2), "=", number1 * number2)
    answer = number1 * number2

elif function == "/":
    print(str(number1), "/", str(number2), "=", number1 / number2)
    answer = number1 / number2

else:
    print("That isn't a valid function in this program!")

time.sleep(1.5)

round_number = input("Would you like to round your number the nearest hundredth decimal(answer with yes or no)?:")

if round_number == "yes":
    print(answer, "rounded to the nearest hundredth is", round(answer, 2))


elif round_number == "no":
    print("Ok :)")

