#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Write your code here
    class DoublyLinkedListNode():
        def __init__(self, data):
            self.digit = len(data)
            self.data = data
            self.prev = None
            self.next = None

    class DoublyLinkedList():
        def __init__(self):
            self.head = None
            self.tail = None

        def insert_node(self, data):
            node = DoublyLinkedListNode(data)

            if not self.head:
                self.head = node
            else:
                self.tail.next = node
                node.prev = self.tail

            self.tail = node

        def sort_node(self, node_1, node_2):
            if (node_1.digit < node_2.digit) or (node_1.digit == node_2.digit and node_1.data < node_2.data):
                if node_2.prev:
                    node_2.prev.next = node_1
                if node_1.next:
                    node_1.next.prev = node_2
                node_1.prev = node_2.prev
                node_2.prev = node_1
                node_2.next = node_1.next
                node_1.next = node_2
                if node_1 == self.tail:
                    self.tail = node_2
                if node_2 == self.head:
                    self.head = node_1
                    return False
                return True
            else:
                return False

    linked_list = DoublyLinkedList()
    for value in unsorted:
        linked_list.insert_node(value)
        if linked_list.head != linked_list.tail:
            new_node = linked_list.tail
            while True:
                if not linked_list.sort_node(new_node, new_node.prev):
                    break

    sorted_list = []
    node = linked_list.head
    while node:
        sorted_list.append(node.data)
        node = node.next
    return sorted_list

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input_txt = open('test_case/Big Sorting-0.txt', 'r')

    n = int(input_txt.readline().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input_txt.readline().strip()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')
    print(result)

    # fptr.close()
