"""
Write a python script to check whether a given year is a leap year or not
"""
year=int(input("Enter a year : "))

if year%4==0 or year%400==0:
    print("year %d is  a leap year"%year)
else:
    print("year %d is not a leap year"%year)