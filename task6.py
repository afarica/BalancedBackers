#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
brackets={'}':'{',
        "]":"[",
        ")":"("}
    
def isBalanced(s):
    a=list()
    for c in s:
        if a and a[-1]==brackets.get(c):
            a.pop()
        else:
            a.append(c)
    if a:
        return 'NO'
    else:
        return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
