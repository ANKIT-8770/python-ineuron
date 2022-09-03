"""
Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
"""

a=int(input("enter first number : "))
b=int(input("Enter second number : "))

if a>b:
    print("first number %d is greater"%a)
elif b>a:
    print("second number %d is greater"%b)
elif a==b:
    if a%2==0:
        print("even number is %d"%a)
else:
    print("invalid input")