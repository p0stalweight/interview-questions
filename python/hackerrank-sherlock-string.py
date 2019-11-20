#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.


def isValid(s):
    char_count = {}

    # Add all characters to hash table
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    # Verify all counts are the same, or with one exception
    count_check = char_count[s[0]]  # intialize to a value
    char_removed = False
    for c in char_count:
        if char_count[c] == count_check:
            continue
        elif (char_count[c] == count_check + 1) and not char_removed:
            char_removed = True
        elif (char_count[c] == count_check - 1) and not char_removed:
            char_removed = True
        elif char_count[c] == 1 and not char_removed:
            char_removed = True
        else:
            return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
