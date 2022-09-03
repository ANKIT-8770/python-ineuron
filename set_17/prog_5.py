"""
Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}

"""

secondset={"C", "Cpp", "NoSQL"}
hisset ={"Java", "Python", "SQL"}
l1=list(secondset)

for e in l1:
    hisset.add(e)
print(hisset)




