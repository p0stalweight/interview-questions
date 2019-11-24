#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
# Print YES if balanced, NO if unbalanced
def isBalanced(s):

    # String length must be even
    if len(s) % 2 != 0:
        return "NO"

    # Strings containing valid bracket
    left_bracket = "({["
    right_bracket = ")}]"

    stack = []
    balanced = True
    i = 0

    while balanced and i < len(s):
        ch = s[i]
        i += 1

        # Determine if character is a left or right bracket
        if left_bracket.find(ch) != -1:
            stack.append(ch)

        # For right bracket, verify stored character is complement
        elif right_bracket.find(ch) != -1:

            if ch == ')':
                if not (len(stack) > 0 and stack.pop() == '('):
                    balanced = False

            elif ch == '}':
                if not (len(stack) > 0 and stack.pop() == '{'):
                    balanced = False

            elif ch == ']':
                if not(len(stack) > 0 and stack.pop() == '['):
                    balanced = False

    if balanced and not stack:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
