# Write a program to find the sum of the 
# first `n` natural numbers.

# **Example**:

# Input: `n = 10`

# 1+2+3+4+5+6+7+8+9+10=55

# Output: `Sum = 55`
n=int(input("Enter your value: "))
output = 0
for i in range (1,n+1):
    output = output+i
print(f"{output} is your sum")
