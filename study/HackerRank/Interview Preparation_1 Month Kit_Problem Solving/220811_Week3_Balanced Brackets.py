#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    def get_balanced_bracket(left_bracket):
        if left_bracket == '(':
            return ')'
        elif left_bracket == '{':
            return '}'
        elif left_bracket == '[':
            return ']'
        else:
            return None

    s = list(s)
    pnt = 0
    while len(s):
        if s[pnt] in ['(','{','[']:
            pnt += 1
            if len(s) == pnt:
                return 'NO'
        else:
            if get_balanced_bracket(s[pnt-1]) != s[pnt]:
                return 'NO'
            else:
                s.pop(pnt-1)
                s.pop(pnt-1)
                pnt -= 1
    return 'YES'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Balanced Brackets-9.txt', 'r')

    t = int(input_txt.readline().strip())

    for t_itr in range(t):
        s = input_txt.readline().strip()

        result = isBalanced(s)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
