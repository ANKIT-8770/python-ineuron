"""
Que-1 Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)
"""
# num=int(input("enter a number : "))
# print(int(num/10))    # output is 253 if input is 2534

"""
Que-2 Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9)
"""
# num=int(input("Enter a number : "))
# print(num%10)    #output is 9 if input is 2089

"""
Que-3 Write a python script to swap data of two variables
"""
# a=eval(input("Enter the value of a : "))
# b=eval(input("Enter the value of b : "))
# print("Before swapping\n The value of a is : ",a,"\n And The value of b is : ",b)
# temp=a
# a=b
# b=temp
# print("After swapping\n The value of a is : ",a,"\n And The value of b is : ",b)

"""
Que-4 Write a python script to find x power y, where values of x and y are given by user
"""
# x=int(input("Enter the value of x : "))
# y=int(input("Enter the value of y : "))
# print("the result of ",x,"to the power of ",y," is ",x**y)


"""
Que-5 Write a python script which takes a three digit number from the user and displays
only its first digit.
"""
# num=int(input("Enter a three digit number : "))
# print(int(num/100))

"""
Que-6 Write a python script which takes a three digit number from the user and displays
only its middle digit.
"""
# num=int(input("Enter a three digit number : "))
# d=int(num/10)
# result=d%10
# print("the middle digit is ",result)

"""
Que-7 Write a python script which takes a three digit number from the user and displays
only its last digit.
"""
# num=int(input("Enter a three digit number : "))
# print("the last digit is : ",num%10)

"""
Que-8 Write a python script to use IN operator to display the data present in the list
"""
# x="ankit patel"
# print("k" in x)  #True
# print("o" in x)  #False

"""
Que-9 Write a python script to use NOT IN operator to display the data not present in list
"""
# y="12344"
# print("9" not in y)  #True

"""
Que-10 Write a python script to use IS operator to display if both variables are the same
object or not?
"""
x=10
y=10
print(x is y)   #True 
print(id(x))    #1220891968016   
print(id(x))    #1220891968016
#both the variable have same id hence both have same object


