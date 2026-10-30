# import random 
# ls = ["ad", "fg", "uu", "wr"]
# x = random.choice(ls) 
# print(x) --> choosing a random item from the list 


# import random 
# ls = ["ad", "fg", "uu", "wr"]
# x = random.choice(ls) 
# print(x) 



# import random 
# x = random.choice("himanshu") 
# print(x) --> choose a random letter from the word. 




# #TURTLE: 
# import turtle 

# screen =  turtle.Screen() 

# screen.bgcolor("green") 

# arrow = turtle.Turtle() 
# arrow.pencolor("white") #change color of arrow 
# arrow.pensize(5) #change arrow thickness 

# for i in range(4): #will repeat 4 times 
#     arrow.forward(200) #change length of arrow
#     arrow.left(90) #arrow will move 90 degree left 

# turtle.mainloop


#TURTLE project: 
# import random 
# colorList = ["yellow","red","green","blue","white"]

# import turtle

# screen = turtle.Screen()

# screen.bgcolor("black")


# arrow = turtle.Turtle()
# arrow.pensize(7)
# arrow.speed(0)
# for i in range(100):
#     arrow.pencolor(random.choice(colorList))
#     arrow.forward(i*2)
#     # arrow.left(120) #You are moving left, so you have to do 180 - 60 = 120 
#     arrow.right(144)  #When you are moving right OR left, you have to do the total number of angles - the desired angle. --> 180 - 36 = 144 
  
    

# turtle.mainloop()


#class 21: 
from turtle import * 
import turtle
import random 
arrow = Turtle () 
arrow.speed(0)
listOfColor = ["red", "green", "blue", "white"] 
arrow.penup()
x=-350
y=300
while True: 
    arrow.goto(x=x, y=y) #go diagonal 
    x +=1 
    if x <= -350: 
        arrow.penup#make it turn right once it reaches diagonal 
     #will keep going down 

turtle.done
