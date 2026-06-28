#Write a program to calculate the factorial of a number using a loop.

#**Example**:

#Input: `n = 5`

#1*2*3*4*5 = 120

#Output: `Factorial = 120

n=int(input("Enter your value: "))
output = 1
for i in range (1,n+1):
    output = output * i 
print(f"{output} is your sum")
