"""
 Write a python program to create a function to check whether a string is a pangram
or not


"""

def pangram(str):
    if str.isalpha():
        print("string is a pangram")
    else:
        print("string is not a pangram")


str=input("Enter a string : ")
pangram(str)

   