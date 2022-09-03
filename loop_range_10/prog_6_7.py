#Write a python script to print first N even natural numbers

N=int(input("enter the N : "))
r=range(2,N*2+1,2)
for x in r:
    print(x)

""" if input is 5

2
4
6
8
10

""" 

#Write a python script to print first N even natural numbers in reverse order
N=int(input("enter the N : "))
r=range(N*2,0,-2)
for x in r:
    print(x)