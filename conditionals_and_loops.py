#### False in Python  #####
print(False is False)
print(None is False)
print(int(0) is False)
print(float(0.0) is False)
print("" is False)          # empty string
print([] is False)          # empty list/array
print(() is False)          # empty tuple
print({} is False)          # empty dict/hash
print(set() is False)       # empty set
print()
###
num = 5
if (num%2) == 0:
  print('I like ' + str(num))
else:
  print('I\'m ambivalent about ' + str(num))
###
print()
#### Handling exceptions
def get_number_from_user():
  input_is_invalid = True
  while input_is_invalid:
    num = input('Please enter a whole number: ')
    try:
       num = int(num)
       print('whole!')
       # Won't get here if exception is raised. '
       input_is_invalid = False
    except ValueError:
       print(num + ' is not a whole number. Try again.')
  return num

get_number_from_user()
print()
####
houses = ["Stark", "Lannister", "Targaryen"]
h = list(map(lambda house: house.upper(), houses))
print(h)
print()
####  filter
nums = [0,1,2,3,4,5,6,7,8,9]
f = list(filter(lambda x: x % 2 == 0, nums))
print(f)
print()
#### Comprehensions
grades = [100, 90, 0, 80]
print([x for x in grades])list()
print([x+5 for x in grades])
print()
#####
words = ["Winter is coming", "Hear me roar", "Fire and blood"]
g = list(zip(houses, words))
print(g)
print(type(g)) # list/array
print()
###
house2words = {house: words for house, words in zip(houses, words)}
print(house2words)
print(type(house2words))  # dict/hash
print()
###
z = dict(zip(houses, words))
print(z)
print(type(z))
print()
###
import functools
d = functools.reduce(lambda x, y: x * y, [1,1,2,3,4,5,6,7,8,9]) # 
print(d)
print()
##
a1 = functools.reduce(lambda x, y: x * y, [1,2,3,4,5])
a2 = functools.reduce(lambda x, y: x * y, range(1,6))
print(a1)
print(a2)  # 
print()



















