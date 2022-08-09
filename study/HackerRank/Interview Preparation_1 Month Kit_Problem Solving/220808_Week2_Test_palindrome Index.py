import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
  # Write your code here
  # if s == s[::-1]:
  #   return -1
  # for i in range(len(s)):
  #   q = s[0:i] + s[(i+1):]
  #   if q == q[::-1]:
  #     return i
  # return -1
  for i in range(0,int(len(s)/2)):
    if s[i] != s[len(s) - i - 1]:
      q = s[0:i] + s[(i+1):]
      if q == q[::-1]:
        return i
      r = s[0:(len(s) - i - 1)] + s[(len(s) - i):]
      if r == r[::-1]:
        return len(s) - i - 1
  return -1

if __name__ == '__main__':
  s_list = [
    'quyjjdcgsvvsgcdjjyq',
    'hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh',
    'fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf',
    'bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb',
    'fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf',
    'mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm',
    'tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt',
    'lhrxvssvxrhl',
    'prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp',
    'kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk'
    ]
  for s in s_list:
    print(palindromeIndex(s))
