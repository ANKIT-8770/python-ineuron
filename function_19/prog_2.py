"""
Write a python program to create a function which expects two arguments and print
them in the function body.
"""
def add(a,b):
    c=a+b
    print("sum of %d + %d = %d"%(a,b,c))

x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
add(x,y)
