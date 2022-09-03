"""
Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
"""

from re import S


firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

secondlist.append(firstlist)
print(secondlist)