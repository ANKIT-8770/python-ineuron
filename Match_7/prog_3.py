"""
Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.

"""

from socket import CAN_BCM_TX_SETUP


print("Enter first side of triangle : ")
a=int(input())
print("Enter second side of triangle : ")
b=int(input())
print("Enter third side of triangle : ")
c=int(input())

if a**2+b**2==c**2:
    print("right angled triangle")



elif a==b and b==c and c==a:
    print("equilateral triangle")

elif a==b:
    print("isosceles triangle")

else : 
    print("invalid lenght")





