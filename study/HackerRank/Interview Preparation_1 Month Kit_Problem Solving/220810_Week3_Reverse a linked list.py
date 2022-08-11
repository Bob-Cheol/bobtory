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
            print(sep, end='')

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    reverse_llist = SinglyLinkedList()

    while llist:
        reverse_node = SinglyLinkedListNode(llist.data)
        if not reverse_llist.tail:
            reverse_llist.tail = reverse_node
        else:
            reverse_node.next = reverse_llist.head

        reverse_llist.head = reverse_node
        llist = llist.next

    return reverse_llist.head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Reverse a linked list-0.txt','r')

    tests = int(input_txt.readline())

    for tests_itr in range(tests):
        llist_count = int(input_txt.readline())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input_txt.readline())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ')
        # fptr.write('\n')

    # fptr.close()
    input_txt.close()
