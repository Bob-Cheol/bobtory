#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    def getMostFreq(num_list):
      num_list_unique = list(set(num_list))
      count_list = []
      for n_num in num_list_unique:
        count_list.append(num_list.count(n_num))
      return num_list_unique[count_list.index(max(count_list))]
    s_list = list(s)
    s_set = set(s_list)
    s_count = list()
    for s_chr in s_set:
        s_count.append(s_list.count(s_chr))
    print(s_count)
    most_freq_count = getMostFreq(s_count)
    over_count = 0
    for s_num in s_count:
      if s_num == most_freq_count:
        continue
      elif s_num == 1 or s_num - 1 == most_freq_count:
        over_count += 1
        if over_count > 1:
          return 'NO'
      else:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
