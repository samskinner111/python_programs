global_hello = 'Bonjour'
def global_hello():
  print('This is the global_hello() function.')

print(global_hello)  ## what does the response illustrate?
###
greeting = "Hi, All!"
def greet(ting):
  print(ting)

greet(greeting)  
###
def greet(name, greeting, number):
  print((greeting  + ', ') * number + name)

greet('Sam', 'Hey', 3)
greet('Bill', number = 4, greeting="Hiya")
####
def echo(*args):
  print(args)

echo(1, "red_fish", 2, "blue_fish")
###
def print_dict(**kwargs):
  print(kwargs)

print_dict(a=1, steak='sauce')
###
def g():
  print('man')

fbi = g()  
print(type(fbi))
###
def factorial(n):
  def fac_iter(n, accum):
    if n <= 1:
        return accum
    return fac_iter(n - 1, n * accum)
  return fac_iter(n, 1)

print(factorial(90))
###
def by_gpa(stud):
  return stud[1]

studs = [("Stan", 2.5, "ISyE"), ("Kyle", 2.2, "CS"), ("Stan", 2.1, "CS"),
         ("Cartman", 2.4, "CmpE"), ("Kenny", 4.0, "ME")]

print(sorted(studs))  # sorts by name then by number 
print(sorted(studs, key=by_gpa, reverse=True))  # key sorts by gpa
print()
print(sorted(studs, key=lambda x: x[2])) # defines sort key by index in array



















  