"""
Write a python program to create a function which expects an unknown number of
arguments.
"""




def f1(*t):
   for e in t:
      print(e,end=" ")
   print()

f1(10,20,30)
f1(1,3,2,4,5,6,8,7)



