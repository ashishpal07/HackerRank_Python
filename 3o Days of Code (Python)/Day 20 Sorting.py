#Day 20 Sorting

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swap = 0
for i in range(len(a)):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swap += 1

print("Array is sorted in {} swaps.".format(swap))
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])
           
