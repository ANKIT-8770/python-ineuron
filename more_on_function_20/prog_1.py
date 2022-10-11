"""
Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements.
"""
def fun(l1):
    l2=["patel",555]
    for e in l1:
        l2.append(e)
    
    return l2
 
l1=[2,4,5,"ANkit"]
print("new list is ",fun(l1))