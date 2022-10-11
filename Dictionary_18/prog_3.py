"""

Write a python program to get a list of the values from a dictionary.

"""

d1={"name":"ankit patel","age":20,"gender":"male"}

l1=[d1[e] for e in d1]
print(l1)
       #['ankit patel', 20, 'male']