"""
Write a python program to create a dictionary that contains three dictionaries.
(nested)

"""

d={
   1: {"name1":"ankit","name2":"pranshu","name3":"nitesh"},
   2:{"age1":20,"age2":21,"age3":19},
   3:{"gender1":"male","gender2":"male","gender3":"male"}
 }

print(d[1])           #{'name1': 'ankit', 'name2': 'pranshu', 'name3': 'nitesh'}
print(d[1]["name1"])  #ankit

