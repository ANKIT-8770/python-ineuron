"""
Write a python program to create a function to check whether a given number is even
or odd

"""
def even_odd(num):
    if num%2==0:
        print("Number %d is even"%num)
    else:
        print("Numeber %d is odd"%num)

num=int(input("Enter a number : "))
even_odd(num)