#assignment 1: 
def showWord(n):
    if n == 0:
        return
    print("Python")
    showWord(n - 1)

showWord(4)
showWord(0)


#assignment 2: 
def countByTwo(n): 
    if n <= 0: 
        return 
    print(f"{n}") 
    countByTwo(n-2)
countByTwo(8)


#Assignment 3: 
def show_word(n):
    if n == 0:
        return
    print("Python")
    show_word(n - 1)

show_word(2)
    

    