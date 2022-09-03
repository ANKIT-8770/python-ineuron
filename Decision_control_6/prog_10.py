"""
 Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same
"""
a=int(input("enter a value of a : "))
b=int(input("enter a value of b : "))
c=int(input("enter a value of c : "))

if (a>b) and (a>c):
    print("number a=%d is greater"%a)
elif b>c:
    print("number b=%d is greater"%b)
elif a==b and b==c:
    
        print("even")
else:
    print("number c=%d is greater"%c)
