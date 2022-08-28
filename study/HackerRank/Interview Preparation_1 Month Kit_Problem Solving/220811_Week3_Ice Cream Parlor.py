#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    for i in range(len(arr)):
      try:
        j = arr[(i + 1):].index(m - arr[i]) + i + 1
        result = list({i + 1, j + 1})
        result.sort()
        return result
      except:
        pass

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Ice Cream Parlor-0.txt', 'r')

    t = int(input_txt.readline().strip())

    for t_itr in range(t):
        m = int(input_txt.readline().strip())

        n = int(input_txt.readline().strip())

        arr = list(map(int, input_txt.readline().rstrip().split()))

        result = icecreamParlor(m, arr)

        # fptr.write(' '.join(map(str, result)))
        print(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
