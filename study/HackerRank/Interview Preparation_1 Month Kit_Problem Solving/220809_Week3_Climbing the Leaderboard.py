#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = list(set(ranked))
    ranked.sort()
    ranked = ranked[::-1]

    def compareWithMid(first_index,last_index,score):
        mid_index = int((last_index + first_index)/2)
        print(first_index,last_index,mid_index,ranked[mid_index],score)
        if ranked[mid_index] == score:
            return mid_index
        elif ranked[mid_index] < score:
            if ranked[mid_index-1] > score:
                return mid_index
            elif mid_index-1 == first_index and ranked[first_index] < score:
                return first_index
            return compareWithMid(first_index,mid_index,score)
        else:
            if ranked[mid_index+1] < score:
                return mid_index+1
            elif mid_index+1 == last_index and ranked[last_index] > score:
                return last_index+1
            return compareWithMid(mid_index+1,last_index,score)

    result_list = list()
    for score in player:
        result_list.append(
            compareWithMid(0,len(ranked)-1,score) + 1
        )
    return result_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # input_txt = open('study/HackerRank/Interview Preparation_1 Month Kit_Problem Solving/test_case/Climbing the Leaderboard-2.txt','r')
    input_txt = open('./test_case/Climbing the Leaderboard-2.txt','r')

    ranked_count = int(input_txt.readline().strip(' '))

    ranked = list(map(int, input_txt.readline().rstrip().split(' ')))

    player_count = int(input_txt.readline().strip(' '))

    player = list(map(int, input_txt.readline().rstrip().split(' ')))

    result = climbingLeaderboard(ranked, player)
    print(result)

    # # fptr.write('\n'.join(map(str, result)))
    # # fptr.write('\n')

    # # fptr.close()
