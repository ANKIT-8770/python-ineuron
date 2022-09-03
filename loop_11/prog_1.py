#Write a python script to calculate sum of first N natural numbers

N=int(input("enter the value of N : "))
sum=0
r=range(1,N+1)
for x in r:
    sum=sum+x
print("The sum of first N natural number is : ",sum)