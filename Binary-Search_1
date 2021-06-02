import random


def bin_search(array,value):
    start=0
    end= len(array)-1
    mid=(start+end)//2
    while not(array[mid]==value) and start<=end:
        if value < array[mid]:
            end=mid-1
        elif value > array[mid]:
            start = mid+1
        mid=(start+end)//2
        print(start, mid, end)
    if array[mid]==value:
        return mid
    else:
        return -1
        
        


#Generate 100 random numbers between 1 and 1000
randomlist = random.sample(range(1, 1000), 100)
randomlist.sort()
print(randomlist)
a = int(input())
print(bin_search(randomlist,a))

