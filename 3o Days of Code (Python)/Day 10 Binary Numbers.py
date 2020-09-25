#Day 10 Binary Numbers

#!/bin/python3

import math
import os
import random
import re
import sys



#if __name__ == '__main__':

    n = int(input())
    s = bin(n)[2:]
    k = s.split('0')
    print(k)
    print(max(map(len,k)))

