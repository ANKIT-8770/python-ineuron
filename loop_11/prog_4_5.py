#Write a python script to calculate sum of first N odd natural numbers

N=int(input("Enter the value of N : "))
sum=0
r=range(1,N*2+1,2)
for x in r:
      sum=sum+x
print("The sum of first ",N," odd natural numbers : ",sum)




#Write a python script to calculate sum of first N even natural numbers

N=int(input("Enter the value of N : "))
sum=0
r=range(0,N*2+1,2)
for x in r:
      sum=sum+x
print("The sum of first ",N," even natural numbers : ",sum)




















#Write a python script to calculate sum of first N even natural numbers