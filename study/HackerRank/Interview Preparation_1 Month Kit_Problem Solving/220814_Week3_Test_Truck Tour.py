#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    class DoublyLinkedListNode():
      def __init__(self, index, data):
        self.index = index
        self.data = data
        self.prev = None
        self.next = None

    class DoublyLinkedList():
      def __init__(self):
        self.head = None
        self.tail = None

      def insert_node(self, index, data):
        if not self.head:
          node = DoublyLinkedListNode(index, data)
          self.head = node

          self.tail = node
          self.tail.next = self.head
          self.head.prev = node
        elif self.tail.data * data >= 0:
          self.tail.data += data
        else:
          node = DoublyLinkedListNode(index, data)

          self.tail.next = node
          node.prev = self.tail

          self.tail = node
          self.tail.next = self.head
          self.head.prev = node

    pump_list = DoublyLinkedList()
    for i in range(len(petrolpumps)):
      pump_list.insert_node(i, petrolpumps[i][0] - petrolpumps[i][1])

    pump = pump_list.head
    while True:
      if pump.prev.data < 0 and pump.data >= 0:
        sub_pump = pump
        sub_sum = 0
        while sub_sum >= 0:
          sub_sum += sub_pump.data
          sub_pump = sub_pump.next
          if sub_pump.index == pump.index:
            return pump.index
      pump = pump.next

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Truck Tour-0.txt', 'r')

    # n = int(input().strip())
    n = int(input_txt.readline().strip())

    petrolpumps = []

    for _ in range(n):
        # petrolpumps.append(list(map(int, input().rstrip().split())))
        petrolpumps.append(list(map(int, input_txt.readline().rstrip().split())))

    result = truckTour(petrolpumps)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()
