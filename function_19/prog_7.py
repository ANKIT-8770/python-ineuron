"""
Write a python program to sum all the numbers in a list.
"""



def summ(list1):
    sum=0
    for e in list1:
        sum=sum+e
    return sum

list1=[3,4,5,6,7,1]
print("sum of all number in a list is ",summ(list1))