#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    mid = int((len(s) - 1)/2)
    f = s[0:(mid+1)]
    b = s[(mid+1):]
    f_list = list(f)
    b_list = list(b)
    for f_chr in f_list:
        try:
            b_list.remove(f_chr)
        except:
            continue
    return len(b_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
