#Write a python script to check whether a given number is Prime or not

n=int(input("enter a  number : "))

r=range(2,int(n/2)+1)
for i in r:
    if (n%i)==0:
        print("not a prime")
        break
else:
   print("prime")
