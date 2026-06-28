n = int(input("Enter n: "))
nIsPrime = True
for i in range(2,n): 
    rem = n % i 
    if rem == 0 :
        print(f"{n} is not a prime number")
        nIsPrime = False
        break
    if nIsPrime == True: 
        print(f"{n} is a prime")

