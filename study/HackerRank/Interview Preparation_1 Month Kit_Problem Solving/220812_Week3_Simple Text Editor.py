
def simple_text_editor(ops):

  def append_word(text, w):
    return text + w

  def delete_words(text, n):
    return text[0:(len(text)-n)]

  def print_word(text, n):
    print(text[n-1])
    # return text[n-1]

  def undo(text_list):
    return text_list[0:-1]

  s_list = ['']
  # result = ''
  for o_itr in range(len(ops)):
    query = ops[o_itr].split(' ')
    if query[0] == '1':
      s_list.append(append_word(s_list[-1],query[1]))
    elif query[0] == '2':
      s_list.append(delete_words(s_list[-1],int(query[1])))
    elif query[0] == '3':
      print_word(s_list[-1],int(query[1]))
      # result = result + print_word(s_list[-1],int(query[1])) + '\n'
    elif query[0] == '4':
      s_list = undo(s_list)

  # return result

if __name__ == '__main__':
  # fptr = open('result.txt', 'w')
  input_txt = open('test_case/Simple Text Editor-7.txt', 'r')

  q = int(input_txt.readline().strip())

  ops = list()

  for q_itr in range(q):
    ops.append(input_txt.readline().strip())

  simple_text_editor(ops)
  # result = simple_text_editor(ops)

  # fptr.write(result)

  # fptr.close()
