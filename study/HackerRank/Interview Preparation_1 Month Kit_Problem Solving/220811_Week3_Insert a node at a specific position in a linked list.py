#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        # fptr.write(str(node.data))
        print(str(node.data), end = '')

        node = node.next

        if node:
            # fptr.write(sep)
            print(sep, end = '')

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    node = SinglyLinkedListNode(data)
    first_node = llist

    if position == 0:
      node.next = llist
      first_node = node
    else:
      for i in range(position-1):
        llist = llist.next

      node.next = llist.next
      llist.next = node

    return first_node

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Insert a node at a specific position in a linked list-0.txt', 'r')

    llist_count = int(input_txt.readline())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input_txt.readline())
        llist.insert_node(llist_item)

    data = int(input_txt.readline())

    position = int(input_txt.readline())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ')
    # fptr.write('\n')

    # fptr.close()
