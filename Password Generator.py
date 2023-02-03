import random
import string

print("\n Welcome To Password Generator \n")

length = int(input("\n Enter A Length of Password: "))

upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase
numberCase = string.digits
symbolCase = string.punctuation

pas = upperCase + lowerCase + numberCase + symbolCase

word = random.sample(pas, length)

ps = "".join(word)

print("Password: ", ps)