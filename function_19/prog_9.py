"""
Write a python program to create a function to check whether a number falls in a
given range
"""
def ran():
    for e in range(1,5):
        print(e,end=' ')
    print()
    print("I think your doubt has been cleared......[Y/N] ")
    c=input()
    if c=='Y':
        pass


def check(num):
    for e in range(1,5):
        if num==e:
            print("number in present in a range")
            break
    else:
        print("number is not available in a given range")

    print("you have any doubt [y/n]")
    d=input()
    if d=='y':
        print("check the number that you entered ...")
        ran()
    else:
        pass

num=int(input("enter a number : "))
check(num)
