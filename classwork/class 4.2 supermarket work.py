total = int(input("Enter your total amount: "))
code = str(input("Enter your code: "))
if total > 500:
    total = total - total*5/100
if code == "SAVE10": 
    total = total - 50 
else: 
    print("the code you gave is NOT correct, and is not elligible for a discount")
print(f"{total} is your final amount")