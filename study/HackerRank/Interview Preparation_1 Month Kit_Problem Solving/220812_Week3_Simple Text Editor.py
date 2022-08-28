from datetime import datetime

class DoublyLinkedListNode():
  def __init__(self, data):
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

def simple_text_editor(text_list, query):
  query_list = query.split(' ')
  if query_list[0] == '1':
    if not text_list.tail:
      text_list.insert_node(query_list[1])
    else:
      text_list.insert_node(text_list.tail.data + query_list[1])
  elif query_list[0] == '2':
    text_list.insert_node(text_list.tail.data[0:(len(text_list.tail.data) - int(query_list[1]))])
  elif query_list[0] == '3':
    print(text_list.tail.data[int(query_list[1]) - 1])
  elif query_list[0] == '4':
    text_list.tail = text_list.tail.prev
    if not text_list.tail:
      text_list.head = None
      text_list.tail = None
    else:
      text_list.tail.next = None

if __name__ == '__main__':
  input_txt = open('test_case/Simple Text Editor-7.txt', 'r')

  q = int(input_txt.readline().strip())

  text_list = DoublyLinkedList()

  print(datetime.now())
  for q_itr in range(q):
    simple_text_editor(
      text_list,
      input_txt.readline().strip()
    )
  print(datetime.now())
