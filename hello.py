# Print a sting with a variable: must convert the varaible to a string.
exam1 = 95
exam2 = 87
exam3 = 99

exam_avg = (exam1+exam2+exam3)/3
exam_avg = round(exam_avg, 1)
exam_avg = str(exam_avg)
grade_report = "Your exam average is " 

print(grade_report + exam_avg)

#String concatenation
print("Yo" + "lo")

#Class type
print(type(3.14))
print(type('pig'))
print(3 * "Yo")  # "you" * 3

# Python reserved words:                
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise   

# Type conversions, some weird
print(int(2.9))     # 2
print(float(True))  # 1.0
print(int(False))   # 0
print(str(True))    # "True"

# Multi-line strings:
print("""This will print as
a multi-line string""")

# String methods
i = 'carrot'
print(len(i))       # 6
print(i[3])         # r
print(i[0] + i[5])  # ct
                    
trump = 'manboorishpig'
print(trump[:3])
print(trump[3:10])
print(trump[10:])

print('frgoobar'.find('o'))  # yields the index of the character

### Exercise: return the username from an email and hostname from a url
email = 'bob@example.com'
url = 'aol.com'

index = email.find('@')
print(email[:index])

index = url.find('.')
print(url[:index])









               