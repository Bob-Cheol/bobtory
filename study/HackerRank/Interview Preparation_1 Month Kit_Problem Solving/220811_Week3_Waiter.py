#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    # Write your code here
    return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Waiter-0.txt', 'r')

    first_multiple_input = input_txt.readline().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input_txt.readline().rstrip().split()))

    result = waiter(number, q)

    # fptr.write('\n'.join(map(str, result)))
    print('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
