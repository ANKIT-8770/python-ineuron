"""
Write a Python script to remove all non int values from a list.

"""

from os import remove


list=[1,"ankit",2,4.5,'23',66]
b=[]
for i in list:
    if type(i)==int:
       b.append(i)

list=b
print(list)