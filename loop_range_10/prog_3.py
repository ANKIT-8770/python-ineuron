#Write a python script to print first N natural numbers in reverse order
#  syntax - 
#   r=range(beg,end,step)  or r=range(beg,end,common_difference)

r=range(int(input("enter value of N : ")),0,-1)
for x in r:
    print(x)

""" if input is 5

5
4
3
2
1


"""


r1=range(1,int(input("enter value of N : "))+1,1)
for x1 in r1:
    print(x1)

"""  if input is 5

1
2
3
4
5
 
"""   