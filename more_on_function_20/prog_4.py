"""
Write a python program to create a function that checks whether a passed string is
palindrome or not.

"""
def palindrome(str):
     
    if str==str[::-1]:
        print("string is palindrome")
        
    else:
        print("string is not a palindrome")

str=input("Enter a string : ")
palindrome(str)

    
