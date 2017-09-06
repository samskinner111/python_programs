dna_text = open('dna.txt')
dna_string = dna_text.read()
dna_string = dna_string.rstrip('\n')  ## removes carriage return at end of string, if present.
print(len(dna_string))
print("The sequence is: " + dna_string + "; it's length is: " + str(len(dna_string)))



















