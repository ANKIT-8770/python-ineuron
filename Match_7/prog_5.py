"""
Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
"""

num=int(input("ENter  a number : "))

match num:
    case num if num%2==0:
        print("Saurabh Shukla ")
    case num if num<0 and num%2!=0:
        print("Prateek Jain")
    case num if num>0 and num%2!=0:
        print(" Aditya Choudhary")
    case _:
        print("invalid number")