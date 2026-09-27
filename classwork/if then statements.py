# create a prog that take number from user
# and it displays whther the number is odd or even
while True:
    number = int(input("Enter your whole number: "))
    remainder = number % 2
    if remainder == 0 :
        print(f"{number} is even")
    else: 
        print(f"{number} is odd")
