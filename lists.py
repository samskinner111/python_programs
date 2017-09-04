men = ['Bill', 'Stan', 'Frank', 'Oscar']
print(men)

empty = [] 
empty1 = list()  # Another way to call an empty list or array.

grades = "90, 87, 42, 56, 100"
print(grades.split())  # Note .split uses whitespace to delimit.
print(grades.split(','))

print(list('abcdefghijklmnopqrstuvwxyz'))

print(men[0])
print(men[-1])
print(men[-2])

men[2] = 'Sam'
print(men)

a = 'Kyle' in men
print(a)

a = 'Kyle' not in men
print(a)

b = 'Sam' in men
print(b)

print(men + ['Kyle'])

print(5*['No'])  # makes a new array!

### List Functions
print(men)
print(len(men))
print(min(men))
print(max(men))
del men[3]
print(men)

### List Methods
surfin_birds = "Bird bird bird b-bird's the word".split()
print(surfin_birds)
print(surfin_birds.count('bird'))  # Capital Bird doesn't count

men.append('Carmen')
print(men)
men.extend(['Alex', 'William', 'Peter'])
print(men)
men.remove('Sam')
print(men)
men.pop()
print(men)
print()
### Slicing works the same as in strings
print(men[:2])
print(men[2:])
print(men[1:3])
### Aliases
boys = men
print(boys)
boys.append('Richie')
print(men)
print()
#Copies
print('Playing with copies and aliases')
print(boys + ['Olen', 'Paul'])
print(boys)
print(men)
boys = boys + ['Olen', 'Paul']
print(boys)
print(men)
print()
### Slicing and Copies
print("Slicing and Copying")
print(men)
first_two = men[:2]
print(first_two)
first_two[0] = "Stan the man"  ## Changes first_two but not men.
print(first_two)
print(men)
###
men[0:2] = ['Sally', 'Rachel', 'Sarah', 'Lilliana']  ## Non-inclusive.
print(men)
print()
### More list/string methods
aretha = ['R', 'E', 'S', 'P', 'E', 'C', 'T']
print("-".join(aretha))
print(" ".join(aretha))
##
print(sorted(aretha))  ## sort
print(aretha)
aretha.sort()    ## sort!
print(aretha)
print() 
### Example: Grades
record = ['Chris', 92, 87, 100]
grades = record[1:]
print(sum(grades))
gpa = sum(grades)/len(grades)
print(gpa)
print()
### Tuples
print('TUPLES')
pair = 1, 3
print(pair)
a, b, c = 1, 2, 4   ## parallel assignment
print(c)
c, a = a, c
print(c)
print()
### Dictionaries (Hashes)
print('DICTIONARIES/HASHES')
capitals = {}
capitals['Georgia'] = 'Atlanta'
capitals['Washington'] = 'Seattle'
print(capitals)
capitals['Washington'] = 'Olympia'
print(capitals)
##
print('Georgia' in capitals)  ## detect key, but not value
print('Atlanta' in capitals)

del capitals['Georgia']
print(capitals)

capitals.update({'Tennessee': 'Nashville', 'Mississippi': 'Jackson'})
print(capitals)
print(capitals.values())
print()
### Conversions to dict/ by dict
print('dict conversions')
a = dict([[1, 1], [2, 4], [3, 9], [4, 16]])
print(a)

b = dict([('Lassie', 'Collie'), ('Rin Tin Tin', 'German Shepherd')])
print(b)

c = dict(['a1', 'a2', 'b3', 'b4'])
print(c)
print()

### Working with Sets
print('WORKING WITH SETS')
names = set()
names.add('Ally')
names.add('Lilly')
names.add('Tilly')
names.add('Sally')
print(names)

d = set([1,2,3,4,3,2,1])  # removes duplicates!
print(d)

### Union and Intersection of Sets
a = {1, 2}
b = {2, 3}
print(a & b)   # intersection
union = a | b  # union
union1 = str(union)
print('The union is ' + union1)  
print( a - b)    # difference (elements in a that are not in b)
print(a ^ b)     # symmetric difference (non-common elements)                                       
d = {1, 2, 3, 4, 5}
print(b <= d)    # is b a subset of d?
print(b < d)     # is b a proper subset of d
print(d >= b)    # is d a superset of b
print(d > b)     # is d a proper superset of b
print()


