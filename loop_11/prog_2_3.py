#Write a python script to calculate sum of squares of first N natural numbers

N=int(input("enter the value of N : "))
sum=0
r=range(1,N+1)
for x in r:
    sum=sum+x**2
print("The  sum of squares of first",N,"natural numbers : ",sum)



#Write a python script to calculate sum of cubes of first N natural numbers

N=int(input("enter the value of N : "))
sum=0
r=range(1,N+1)
for x in r:
    sum=sum+x**3
print("The  sum of squares of first",N,"natural numbers : ",sum)