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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
  mllist = SinglyLinkedList()

  while head1 or head2:
    if not head1:
      node = SinglyLinkedListNode(head2.data)
      head2 = head2.next
    elif not head2:
      node = SinglyLinkedListNode(head1.data)
      head1 = head1.next
    elif head1.data <= head2.data:
      node = SinglyLinkedListNode(head1.data)
      head1 = head1.next
    else:
      node = SinglyLinkedListNode(head2.data)
      head2 = head2.next

    if not mllist.head:
      mllist.head = node
      mllist_head = mllist.head
    else:
      mllist.tail.next = node

    mllist.tail = node

  return mllist_head

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Merge two sorted linked lists-0.txt', 'r')

    tests = int(input_txt.readline())

    for tests_itr in range(tests):
        llist1_count = int(input_txt.readline())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input_txt.readline())
            llist1.insert_node(llist1_item)

        llist2_count = int(input_txt.readline())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input_txt.readline())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
        # fptr.write('\n')

    # fptr.close()
