# import math 
# n= int(input("enter a number")) 
# print(math.factorial(n))  #factorial 
# print(math.pow(2,4))      #rasied to the power of 
# (print(math.gcd(12,18,6))) #greadest common factor
# print(math.sin(90)) #sin for sin in radians: 
# print(math.sin(math.radians(90))) #sin in radians. Same 
# #for tan and cosine 
# print(math.pi) #pi 
# print(math.sqrt(25)) #square root 

# import random 
# x = random.randint(1,10) 
# print(x)                  #pick any random number 

# def rollDice(): 
#     return random.randint(1,6) 
# print(rollDice())        #print any random number using 
                        #defining any function 

#number guessing game 
#computer will pick a random number between 1-100 
#now you will give a chance to the user to guess the number
#if ur number num matches to the computer's number
#you will say "you won!" 
#if num is smaller than the computer's pick you say 
#too small 
#if the num is greater than the computer's pick you say 
#you say 
# keep giving the chance
#Keep counting the number of attempts
#once they guess the number, break the loop 

#break down: 
#1. start with: computer picking a number
#2. Give the user a chance to input a number
#3. if the number is the same as the pick print "you won" 
#and break the loop 
#4. if the number is smaller than the computer: print "too small" 
#resume loop 
#5. if the number is bigger than the computer: print "too big" 
#resume loop 
#6. Print the number of tries each time. 


import random 
pick = random.randint(1,10)
attempt = 0 
while True:
        attempt = attempt + 1  
        human = int(input("Enter your number between 1-100: ")) 
        if human == pick: 
            print("You won!")  
            break
        elif human > pick: 
            print("too big! try again: ")
            print(attempt) 
        elif human < pick: 
             print("too small! try again: ") 
             print(attempt)

