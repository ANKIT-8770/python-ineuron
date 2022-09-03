"""
Write a python script to check whether a given number is a three digit number or not.

"""
from unittest import result


num=int(input("enter a number : "))
result=num//100


if result>0 and result<10:
    print("number is three digit number")
else:
    print("NUmber is not  a three digit number")



