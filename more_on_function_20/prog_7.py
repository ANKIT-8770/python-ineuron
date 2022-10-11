"""
Write a python program to access a function inside a function.

"""
from unittest import result

def sorry():
    
    while True:
     print("ye bhi majak tha...now aap ab mere kbje me h.....")
     


def age1():
    print("majak tha bhai majak")
    print("If you want to listen sorry from me for this type of  majak [Y/N] ")
    re=input()
    if re=='Y' or re=='N':
        sorry()



def fun1(age):
    if age>18 or age<18:
        age1()
    
        
    

age=int(input("Enter your age : "))
fun1(age)