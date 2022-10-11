"""
Write a python program to create a function which expects kwargs arguments.


"""
def fun(a,b,c):
      sum=a+b+c
      print(a,b,c)
      return sum

print("sum is %d"%fun(c=4,b=4,a=1))
