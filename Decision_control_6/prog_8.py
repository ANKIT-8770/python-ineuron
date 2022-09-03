"""
Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
"""

a=int(input("enter a value of a : "))
b=int(input("enter a value of b : "))
c=int(input("enter a value of c : "))

dis=b**2-4*a*c

if dis>0:
    print("both roots are real and distinct")
elif dis==0:
    print("roots are real and equal")
else:
    print("imaginary roots")
