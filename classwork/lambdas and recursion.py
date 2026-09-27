# # #chain of function
# def f1(): 
#     print("hello")
# def f2(): 
#     f1()
#     print("himanshu") 
# def f3():
#     f2()
#     print("bye") 
# f3() 
# #stack memory: When a function call happens, the function is pushed onto the stack. 
# #recursion: when a function calls itself. 
# def f1(): 
#     print("hello") 
#     f1()
# # f1() #Calls itself many times 

# #for reptition we either use loops or recursion 
# for i in range(10): 
#     print("hello",i)  #prints "hello" 10 times

def f1(n):
    #base condition: 
    if n== 1: return 
    print("recursion",n) 
    f1(n-1)
f1(4)  #--> if the number is greater than 1, it will reutn to the function and  print
    #recursion, and since we called it three times it will go up to 3 