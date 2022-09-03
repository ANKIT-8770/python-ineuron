
# Que-1 Write a python script to add comments and print “Learning Python” on screen
print("----------------------------Que-1----------------------\n")
print("Learning Python")


"""
Que-2
Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values.
"""
print("\n----------------------------Que-2--------------------\n")
a=10
b=10.1
c="ankit"
d=True
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))



# Que-3 Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
print("\n----------------------------Que-3--------------------\n")
a=35
b=True
c="MySirG"
d=5.46
e=3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# Que-4 Write a python script to print the id of two variables containing the same integer values.
print("\n----------------------------Que-4--------------------\n")
a=23
b=23
print(id(a))
print(id(b))


# Que-5 Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
print("\n----------------------------Que-5--------------------\n")
a=10
b=10.1
c="ankit"
d=True
print(a,"  ",type(a),"  ",id(a))
print(b,"  ",type(b),"  ",id(b))
print(c,"  ",type(c),"  ",id(c))
print(d,"  ",type(d),"  ",id(d))


# Que-6 Write a python script to print all the keywords
print("\n----------------------------Que-6--------------------\n")
import keyword
print(keyword.kwlist)


# Que-7 On Python shell use help() function and display the list of keywords
print("\n----------------------------Que-7--------------------\n")
help("keyword")


#Que-8 Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the created in A0.py
print("\n----------------------------Que-8--------------------\n")
import assignment_1
print(assignment_1.A)


#Que-9 Name the keywords, used as data in the Python script
print("\n----------------------------Que-9--------------------\n")
k="keywords"
print(k)
print(type(k))


#Que-10 Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)
print("\n----------------------------Que-10--------------------\n")
from datetime import datetime
dt =datetime.today();
print(dt)
d1=dt.strftime("%d-%m-%Y and  %I:%M:%p")
print(d1)

