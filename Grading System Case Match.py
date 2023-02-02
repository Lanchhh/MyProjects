science = int(input("Enter Sciene Grade: "))
filipino = int(input("Enter Filipino Grade: "))
english = int(input("Enter English Grade: "))
math = int(input("Enter Mathematics Grade: "))
comp = int(input("Enter Computer Grade: "))

average = (science + filipino + english + math + comp) / 5

print(average)

match average:
    case average if average > 100:
        print("Invalid Grade")
    case average if average >= 98:
        print("With Highest Honor")
    case average if average >= 95:
        print("With High Honor")
    case average if average >= 89:
        print("With Honor")
    case average if average >= 75:
        print("Passed")
    case _:
        print("Failed")