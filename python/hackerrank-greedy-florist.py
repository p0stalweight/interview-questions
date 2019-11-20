#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.


def getMinimumCost(k, c):
    sum = 0

    # Flowers and customers are equal, buy all the flowers
    # at the original price
    if len(c) == k:
        for i in c:
            sum += i
        return sum

    else:
        remainder = len(c) - k
        
        # Buy most expensive flowers first
        for i in range(remainder, len(c)):
            sum += c[i]

        multiple = 2

        # Continuing buying remaining flowers 
        # most expensive first 
        while remainder > k:
            for i in range(remainder - k, remainder):
                sum += c[i] * multiple
            multiple += 1
            remainder = remainder - k

        if remainder > 0:
            for i in range(0, remainder):
                sum += c[i] * multiple

        return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
