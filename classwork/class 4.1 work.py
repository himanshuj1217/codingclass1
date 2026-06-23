n = int(input("Enter your number: "))
rem_3 = n % 3
rem_5 = n % 5
rem_2 = n % 2
rem_6 = n % 6
if rem_3 == 0 and rem_5 == 0 or rem_2 == 0 and rem_6 == 0: 
    print(f"{n} is divisible by 3 and 5 or 2 and 6")
else: 
    print(f"{n} is not divisible by 3 and 5 or 2 and 6") 
