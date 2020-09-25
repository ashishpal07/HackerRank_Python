#Day 11 2D Arrays

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = []
    #x is row y is column

    for x in range(4):
        for y in range(4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3]) 
            k.append(s)
    print(max(k))
