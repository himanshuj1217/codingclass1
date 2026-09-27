#Assignment 1 
def checkNumbers(*args):
    for i in args:
        if i % 2 == 0:
            print(i, "Even")
        else:
            print(i, "Odd")


checkNumbers(12, 7, 20, 15, 33, 40)

#Assignment 2 

def shoppingList(items):
    items.append("Chocolate")
    items.insert(1, "Juice")
    items.remove("Bread")
    
    print(items)
    print("Total items:", len(items))


#Assignemnt 3
items = ["Milk", "Bread", "Eggs", "Apple"]

shoppingList(items)

def checkMarks(*marks):
    for mark in marks:
        if mark >= 90:
            print(mark, "Excellent")
        elif mark >= 75:
            print(mark, "Very Good")
        elif mark >= 50:
            print(mark, "Pass")
        else:
            print(mark, "Needs Improvement")


checkMarks(95, 82, 67, 43, 91)


def cube(*args):
    for i in args:
        print("Cube of", i, "is", i ** 3)


cube(1, 2, 3, 4, 5)
