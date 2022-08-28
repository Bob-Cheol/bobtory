#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    num_list = list(range(1,int(min(b)/max(a)+1)))
    num_list = [num * max(a) for num in num_list]
    drop_list = list()

    for num in num_list:
        for a_num in a:
            if num % a_num != 0:
                drop_list.append(num)
                break

    for d_num in set(drop_list):
        num_list.remove(d_num)

    drop_list = list()
    for num in num_list:
        for b_num in b:
            if b_num % num != 0:
                drop_list.append(num)
                break
    for d_num in set(drop_list):
        num_list.remove(d_num)

    return len(num_list)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
