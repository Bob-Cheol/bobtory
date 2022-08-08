#!/bin/python3

import math
import os
import random
import re
import sys



#

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
      return -1
    mid = int(len(s)/2)
    a = s[0:mid]
    b = s[mid:]
    alist = list(a)
    blist = list(b)
    for a_num in alist:
      try:
        blist.remove(a_num)
      except:
        pass
    return len(blist)

if __name__ == '__main__':
  s_list = [
    'aaabbb',
    'ab',
    'abc',
    'mnop',
    'xyyx',
    'xaxbbbxx'
  ]
  for s in s_list:
    print(anagram(s))
