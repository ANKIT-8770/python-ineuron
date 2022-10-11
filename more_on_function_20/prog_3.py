"""
Write a python program to create a function that prints the even numbers from a
given list.

  Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

def fun(l1):
    
    for e in l1:
        if e%2==0:
            print(e,end=' ')
        

l1=[1,2,3,4,5,6,7,8,9]
fun(l1)