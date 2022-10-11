"""
Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not.
"""

from tabnanny import check


def check_prime(num):
    
    for i in range(2,(num//2)+1):
        if (num%i)==0:
            print("number %d is not a prime"%num)
            break

    else:
        print("number %d is a prime number"%num)

num= int(input("Enter a number : "))
check_prime(num)