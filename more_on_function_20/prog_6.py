"""
Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30
"""

def fun():
    l1=[ e**2 for e in range(1,31)]
    print(l1)

fun()