
#Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method



n=int(input("enter a number : "))
c=''

while(n>0):
    c=str(c)+str(n%8)
    n=n//8

print(c)
