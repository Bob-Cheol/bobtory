#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    arr_dict = {}
    for i in arr:
      try:
        arr_dict[i] += 1
      except:
        arr_dict[i] = 1
    count = 0
    for value in arr:
      try:
        count += arr_dict[value + k]
      except:
        continue
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Pairs-0.txt', 'r')

    first_multiple_input = input_txt.readline().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input_txt.readline().rstrip().split()))

    result = pairs(k, arr)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()
