n = int(input("enter your input: "))
square = 0 
sum = 0 
for i in range (1,n+1):
    if i%2 == 0 and i%3 == 0:
        square = i**2
        sum = sum + square 
print(f"Your sum is {sum}")
print(36+144+18**2)

