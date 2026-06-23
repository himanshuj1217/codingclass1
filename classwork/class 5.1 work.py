#Inputs:
# - age
# - student (yes/no)

# Rules:

# - Base ticket price = ₹200
# - If age < 12 → 50% discount
# - If student → 20% discount
# - Student discount applies **after** age discount
# - Print final amount.
age = int(input("Enter your age: "))
student = input("Are you a student (yes or no) : ")
ageDiscount = 0
basePrice = 200
finalPrice = basePrice
studentDiscount = 0

if age < 12: 
    ageDiscount = finalPrice * 50/100
    finalPrice = finalPrice - ageDiscount 
else : 
    print(f"{basePrice} is your price without a age discount") 
    

if student == ("yes") : 
    studentDiscount = finalPrice * 20/100 
    finalPrice = finalPrice - studentDiscount 
print (f"""
-------------------------------------------
BASE Price          : {basePrice}
age discount        : {ageDiscount} 
student discount    : {studentDiscount} 
final price         : {finalPrice} 
-------------------------------------------
""") 