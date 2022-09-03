#Write a python script to print first N odd natural numbers

r=range(1,int(input("enter the value of N : "))*2,2)
for x in r:
    print(x)


""" if input is 10

1
3
5
7
9
11
13
15
17
19


"""


#Write a python script to print first N odd natural numbers in reverse order

n=int(input("enter the value of N : "))

r=range(n*2,0,-2)
for x1 in r:
      print(x1-1)


''' if input is 9
17
15
13
11
9
7
5
3
1

'''
  
