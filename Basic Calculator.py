firstNum = int(input("Enter a First Number: "))
secondNum = int(input("Enter a Second Number: "))

oper = input("Select Operator (+, - , * , /): ")

match oper:
    case oper if oper == '+':
        print(str(firstNum), "+", str(secondNum), '=', firstNum + secondNum)
    case oper if oper == '-':
        print(str(firstNum), "-", str(secondNum), '=', firstNum - secondNum)
    case oper if oper == '*':
        print(str(firstNum), "*", str(secondNum), '=', firstNum * secondNum)
    case oper if oper == '/':
        print(str(firstNum), "/", str(secondNum), '=', firstNum / secondNum)
    case _:
        print("Ivalid Operator")