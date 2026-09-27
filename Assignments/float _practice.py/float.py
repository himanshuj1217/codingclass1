original= float(input("Please put in your original price here: "))
discountPercentage= float(input("Please put in your discount percentage here: "))
discountPrice = float( original * discountPercentage / 100 )
finalPrice = float(original-discountPrice)
print(f"""
Your original price is {original}
Your discount percentage is {discountPercentage}
Your discount price is {discountPrice}
Your final price is {finalPrice}
Thank you for shopping with us! 
 """)
