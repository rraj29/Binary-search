import random

# Searching algorithms - Linear Search

def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1



#Generate 100 random numbers between 1 and 1000
randomlist = random.sample(range(1, 1000), 100)
randomlist.sort()
print(randomlist)
a = int(input())
print(linear_search(randomlist,a))
