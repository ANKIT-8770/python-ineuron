"""
Write a python script to print all Prime numbers under 100
"""

for num in range(1,101):
    count=0
    total=0
    for i in range(2, (int(num/2) + 1)):
             if(num%i==0):
                count=count+1
                break

    if count==0 and num!=1:
        total+=1
        print("%d"%num, end=' ')
print(total)
