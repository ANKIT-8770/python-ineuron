
"""
Write a python program to multiply all the numbers in a list.

"""
def multiply(l1):
    result=1
    for e in l1:
        result=result*e
    print("multiplication of all number in a list is ",result)



l1=[1,2,3,4,5]
multiply(l1)
