"""
Write a python program to store all the programming languages known to you using
Set.

"""

from posixpath import split


s=input("Enter all programming languages known to you seperated with comma : ")
s1={eval(e) for e in s.split(',')}
print(s1)