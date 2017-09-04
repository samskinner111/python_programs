######## Part 0 #############
#############################
def strcat_ba(a, b):
    assert type(a) is str
    assert type(b) is str
    return b + a
  
def random_letter():
  from random import choice
  return choice('abcdefghijklmnopqrstuvwxyz')

def random_string(n, fun=random_letter):
  return ''.join([str(fun()) for _ in range(n)])

a = random_string(5)
b = random_string(3)
c = strcat_ba(a, b)
# print(a)
# print(b)
# print(c)
print('strcat_ba("{}", "{}") == "{}"'.format(a, b, c))

########################################
def strcat_list(L):
  assert type(L) is list
  return L[5] + L[4] + L[3] + L[2] + L[1] + L[0]

n = 3
nL = 6
L = [random_string(n) for _ in range(nL)]
Lc = strcat_list(L)
print('L = {}'.format(L))
print('strcat_list(L) == \'{}\''.format(Lc))

######################
import math
a = 14.14
b = 5.97
print(a/b)

c = math.floor(a/b)
print(c)
#########################
def report_exam_avg(nums):
  #assert is_number(a) and is_number(b) and is_number(c)
  exam_avg = str(round(sum(nums)/3, 1))
  return "Your exam average is " + exam_avg
  
grade_report = "Your exam average is " 
msg = report_exam_avg([100, 95, 80])
print(msg)
###########################
def count_word_length(s):
  array = []
  assert type(array) is list
  mad = s.split()
  for word in mad:
    array.append(len(word))
  return array

s = 'the quick brown fox jumped over the lazy dog'
output = count_word_length(s)
print('{}'.format(output))
##
######### Part 1 #############
##
######### Exercse 0 ##########

######### Exercse 1 ##########

######### Exercse 2 ##########

######### Exercse 3 ##########

######### Exercse 4 ##########

##
######### Part 2 #############
##
######### Exercse 0 ##########

######### Exercse 1 ##########

######### Exercse 2 ##########

######### Exercse 3 ##########

######### Exercse 4 ##########

######### Exercse 5 ##########

######### Exercse 6 ##########

######### Exercse 7 ##########















