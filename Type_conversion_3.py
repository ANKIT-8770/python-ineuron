"""
Que-1 Write a python script to convert a number into str type.
"""
num=10
s="ank"
print(str(num))

print("\n================================================\n")

"""
Que-2 Write a python script to print Unicode of the character ‘m’
"""
print("unicode of m is",ord("m"))

print("\n================================================\n")
"""
Que-3 Write a python script to print character representation of a given unicode 100.
"""
print("character of 100 is",chr(100))
print("\n================================================\n")
"""
Que-4 Write a python script to print any number and its binary equivalent
"""
a=10
print(a)
print(bin(a))
print("\n================================================\n")

"""
Que-5 Write a python script to print any number and its octal equivalent.
"""
a=10

print(a)
print(oct(a))

print("\n================================================\n")
"""
Que-6 Write a python script to print any number and its hexadecimal equivalent
"""
a=10
c=10.2
print(a)
print(hex(a)) #you need to use hex() function to convert number into hexadecimal
#print(hex(c)) #it gives error because c is float
print("\n================================================\n")

"""
Que-7 Write a python script to store binary number 1100101 in a variable and print it in
decimal format.
"""
b=0b110101
print("decimal of binary b is ",b) #it will print decimal value ,no need to use any function
print("\n================================================\n")

"""
Que-8 Write a python script to store a hexadecimal number 2F in a variable and print it in
octal format
"""
hexanum=0x2F 
print(oct(hexanum))


print("\n================================================\n")
"""
Que-9 Write a python script to store an octal number 125 in a variable and print it in binary
format.
"""
octalnum=0o125
print(bin(octalnum))   #0b1111101
print("\n================================================\n")

"""
Que-10 Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format
"""
octnum=0o25
hexnum=0x39
sum=octnum+hexnum
print(sum)
print(bin(sum))  #0b1001110