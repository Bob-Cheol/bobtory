# Enter your code here. Read input from STDIN. Print output to STDOUT# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

class SinglyLinkedListNode():
  def __init__(self,data):
    self.data = data
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self,data):
    node = SinglyLinkedListNode(data)

    if not self.head:
      self.head = node
    else:
      self.tail.next = node

    self.tail = node

  def dequeue(self):
    data = self.head.data
    self.head = self.head.next

    return data

  def print_front(self,fptr):
    fptr.write(self.head.data)

if __name__ == '__main__':
  # fptr = open('result.txt', 'w')
  input_txt = open('test_case/Queue using Two Stacks-0.txt', 'r')

  q = int(input_txt.readline().strip())

  qlist = SinglyLinkedList()

  for q_itr in range(q):
    query = input_txt.readline().strip().split(' ')
    if query[0] == '1':
      qlist.enqueue(query[1])
    elif query[0] == '2':
      qlist.dequeue()
    elif query[0] == '3':
      # qlist.print_front(fptr)
      print(qlist.head.data)

  # fptr.close()
