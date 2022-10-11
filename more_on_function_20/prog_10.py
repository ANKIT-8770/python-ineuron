"""
Write a python program to create a function to check whether a string is an anagram
or not
"""

def anagram(str1,str2):

      
      if len(str1)!=len(str2):
        print("two string are not a anagram to each other")
      else:
        
        for i in range(0,len(str1)):
            for s in str1:
               if s not in str2:
                    flag=1
                    break
            else:
              flag=0
    
      if flag==1:
        print("two string are not anagram to each other")
        
      else:
        print("two string are anagram to each other")

        


str1=input("Enter first string : ")
str2= input("Enter second string : ")
anagram(str1,str2)
