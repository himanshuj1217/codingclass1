# ## **3️⃣ Assignment 3 — Electricity Bill**

# Input units consumed.

# Rates:

# - 0–100 units → ₹5 per unit
# - 101–300 → ₹7 per unit
# - 300+ → ₹10 per unit

# Add:

# - If bill > 1500 → 8% surcharge

# Print final 
unitConsumed = int(input("Enter your consumption of units : "))
unit0_100 = 0
unit101_300 = 0 
unit300 = 0 
final = 0 
final_surcharge = 0 

if unitConsumed >= 0 and unitConsumed <=100 : 
    final = unitConsumed * 5
elif unitConsumed >= 101 and unitConsumed <= 300 :
    final = (100 * 5) + (unitConsumed - 100) * 7 
elif unitConsumed >= 300 : 
    final = (100 * 5) + (200 * 7) + (unitConsumed - 300 ) * 10
if final > 1500 : 
    final_surcharge = final * 8/100 
    final = final_surcharge

print(f""" 
        ---------------------Bill breakout------------------------
        Your final cost (plus supercharge if that apllies) is :  {final} 
      
        """)



