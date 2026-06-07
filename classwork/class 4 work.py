#Write a program to take a input from user and find weather the
#number is divisible by 5 and 3 or not
n = int(input("Enter a number: "))
remainder = n % 3 
remainder2 = n % 5
if remainder == 0  and remainder2 == 0:
    print(f"{n} can be divisible by 3 and 5")
else: 
    print (f"{n} can not be divisible by 3 and 5")
