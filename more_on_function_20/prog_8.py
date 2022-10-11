"""
Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters
"""

def fun1(str):
    upper=0
    lower=0
    for e in str:
        if e.isupper():
            upper+=1
        elif e.islower():
            lower+=1
        else:
            pass
    print("number of upper case letter in a given string is ",upper)
    print("number of lower case letter in a given string is ",lower)


str=input("Emter a string : ")
fun1(str)