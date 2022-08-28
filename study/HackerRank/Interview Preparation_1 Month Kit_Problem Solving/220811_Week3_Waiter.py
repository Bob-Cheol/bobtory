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
    def get_prime_number():
        prime_number_list = [2]
        num = 2

        while len(prime_number_list) <= 1200:
            num += 1
            while True:
                for i in range(2,num):
                    if num % i == 0:
                        break
                    elif i == num - 1:
                        prime_number_list.append(num)
                break

        return prime_number_list
    prime_number_list = get_prime_number()
    answer = list()
    for i in range(q):
        delete_num = list()
        for n in range(len(number)):
            if number[n] % prime_number_list[i] == 0:
                answer.append(number[n])
                delete_num.append(n)
        for d in delete_num[::-1]:
            number.pop(d)
        if i != q - 1:
            number = number[::-1]
    answer = answer + number
    return answer

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Waiter-1.txt', 'r')

    first_multiple_input = input_txt.readline().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input_txt.readline().rstrip().split()))

    result = waiter(number, q)

    # fptr.write('\n'.join(map(str, result)))
    print('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
