"""
Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary par
"""

a=int(input("enter a value of a : "))
b=int(input("enter a value of b : "))

cn=complex(a,b)

if cn.real>cn.imag:
    print("real part is greater")
else:
    print("imaginary part is greater")


