menuOption = input("+ - ADD - - SUBTRACT * - MULTIPLY / - DIVIDE: ")

firstNumber = int(input("firstNumber: "))
secondNumber = int(input("secondNumber: "))

if (menuOption == '+'):
    print(firstNumber + secondNumber)
elif (menuOption == '-'):
    print(firstNumber - secondNumber)
elif (menuOption == '*'):
    print(firstNumber * secondNumber)
elif (menuOption == '/'):
    if(secondNumber == 0):
        print("Division by zero no beuono")
    else:
        print(firstNumber / secondNumber)
else:
    print("you have blah blah")


