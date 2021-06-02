# Problem Statement
#Given an array A of N integers, and a target value K. 
#A is sorted in non-decreasing order.
#Write an efficient program to find the start index and the end index of K in A.

#Input
#First line contains two space separated integers N and K
#Second line contains N space separated integers of A

#Output
#Print the starting index and the ending index of K in A separated by a space.
#Print -1 if K is not found in A.

#constraints
#1 <= N <= 3*10^5
#1 <= A[i], K <= 10^9

#Sample Input
# 5 2
# 1 2 2 2 3
#Sample Output
# 1 3

def bin_search(lis,k):
    start = 0
    end= len(lis)-1
    mid=(start+end)//2
    while k!=lis[mid] and start<=end:
        if k>lis[mid]:
            start=mid+1
        else:
            end=mid-1
        mid=(start+end)//2
    if k == lis[mid]:
        i=j=mid
        while i>=0 and lis[i]==k :
            i-=1
        print(i+1,end=" ")
        while j<len(lis) and lis[j]==k:
            j+=1
        print(j-1)
    else:
        print("-1")


a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
bin_search(b,a[1])
