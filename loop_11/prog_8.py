#Write a python script to calculate sum of digits of a given number

n=input("enter a number : ")
sum=0
for x in n:
    sum=sum+int(x)
print("sum of digits of a given number",n,"is",sum)