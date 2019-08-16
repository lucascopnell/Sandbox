"""Lucas Copnell"""

MIN_LENGTH = 3
MAX_LENGTH = 10


password = input("Please enter a Password: ")
while len(password) < 3 or len(password) > 10:
    password = input("Please enter a Password: ")
print(len(password)*"*")
