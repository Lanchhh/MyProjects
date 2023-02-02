science = int(input("Enter Sciene Grade: "))
filipino = int(input("Enter Filipino Grade: "))
english = int(input("Enter English Grade: "))
math = int(input("Enter Mathematics Grade: "))
comp = int(input("Enter Computer Grade: "))

average = (science + filipino + english + math + comp) / 5

print(average)

if average >= 98:
    print("With Highest Honor")
elif average >= 95:
    print("With High Honor")
elif average >= 90:
    print("With Honor")
elif average >= 75:
    print("Passed")
else:
    print("Failed")
