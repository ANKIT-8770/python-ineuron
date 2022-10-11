"""
Write a python program to create a function that finds a maximum of four numbers.
"""

def fun(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>c and b>d:
        return b
    elif c>d:
        return c
    else :
        return d

print("Greater number is ",fun(10000,200,300,3000))