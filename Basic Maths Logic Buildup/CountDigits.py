from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
   if n == 0:
      return 1
   count = 0
   while n>0:
      n//=10
      count+=1
   return count

   """
   def countDigit(n: int) -> int:
   # Write your code here.
   return len(str(n))
   
   
   """