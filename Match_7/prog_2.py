"""
Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division

"""
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("Enter your choice : ")
choice=int(input())

match choice:
    case 1:
        print("Enter first number : ")
        num1=int(input())
        print("Enter second number : ")
        num2=int(input())
        print("Addition of %d  and %d is %d"%(num1,num2,num1+num2))
    
    case 2:
        print("Enter first number : ")
        num1=int(input())
        print("Enter second number : ")
        num2=int(input())
        print("Substraction of %d  and %d is %d"%(num1,num2,num1-num2))
    
    case 3:
        print("Enter first number : ")
        num1=int(input())
        print("Enter second number : ")
        num2=int(input())
        print("Multiplication of %d  and %d is %d"%(num1,num2,num1*num2))

    case 4:
        print("Enter first number : ")
        num1=int(input())
        print("Enter second number : ")
        num2=int(input())
        print("Division of %d  and %d is %d"%(num1,num2,num1//num2))
    
    case _:
        print("Invalid choice")



