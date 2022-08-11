#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        # fptr.write(str(node.data))
        print(str(node.data), end='')

        node = node.next

        if node:
            # fptr.write(sep)
            print(sep, end='')

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # Write your code here
    rev_llist = DoublyLinkedList()

    while llist:
      node = DoublyLinkedListNode(llist.data)

      if not rev_llist.tail:
        rev_llist.tail = node
      else:
        rev_llist.head.prev = node
        node.next = rev_llist.head

      rev_llist.head = node

      llist = llist.next

    return rev_llist.head

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Reverse a linked list-0.txt', 'r')

    t = int(input_txt.readline())

    for t_itr in range(t):
        llist_count = int(input_txt.readline())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input_txt.readline())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ')
        # fptr.write('\n')

    # fptr.close()
