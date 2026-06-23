#--> for i in range(0,15,2): 
    #print(f"hello i:{i} ") 
#-->  square root value of all numbers from 10-50
# for i in range (100,400,1): 
#     print(f"i: {i**(1/2)}")
#--> display all even numbers from 1-100
# for i in range (2,101,2):
#     print(f"i: {i}")
#--> display all numbers that are divisble by 2 and 3. 
# for i in range (1,100,1):
#     remainder = i % 2
#     remainder2 = i % 3
#     if remainder == 0  and remainder2 == 0:
#        print(f"hello i:{i} ")
#--> display all numbers divisible by 2 and 3 or 5 and 10 
for i in range (1,100, 1):
    remainder2 = i % 2
    remainder3 = i % 3
    remainder5 = i % 5
    remainder10 = i % 10
    if remainder2 == 0  and remainder3 == 0 or remainder5 == 0  and remainder10 == 0:
        print(f"hello i:{i} ")