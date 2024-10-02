'''
  Lesson: Math Library 
  Author: Helen Lin
  Date Created: October 2, 2024
  Date Last Modified: October 2, 2024
'''

import math
def q1(): 
  #Write Assignment code here
  num = input("Input a number: ")
  num = float(num)
  print(math.sqrt(num))

def q2(): 
  #Write Assignment code here
  num = input("Input a number: ")
  num = int(num)
  print(math.isqrt(num))

def q3(): 
  #Write Assignment code here
  num = input("Input a number: ")
  num = float(num)
  print(math.floor(num))

def q4(): 
  #Write Assignment code here
  num = input("Input a number: ")
  num = float(num)
  print(math.ceil(num))

def q5(): 
  #Write Assignment code here
  num1 = input("Input a number: ")
  num2 = input("Input another number: ")
  num1 = float(num1)
  num2 = float(num2)
  num = (num1 * num2) / 2 
  print(math.floor(num))


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()
q4()
q5()
