"""
Write a python script to check whether a given number is positive, negative or zero

"""

num=int(input("Enter a number : "))

if num>0:
    print("number %d is positive number"%num)
elif num<0:
    print("number %d is negative"%num)
else :
    print("number is zero")
