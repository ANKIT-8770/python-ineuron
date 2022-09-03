"""
Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

"""
from typing import Tuple


tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple2=()

for i in range(0,len(tuple1),1):
    if(tuple1[i]<tuple1[i+1]):
        tuple2=tuple[i]



