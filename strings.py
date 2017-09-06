# protein = "vlspadktnv"
# y = protein.replace('v', 'y')
# print(y)
# print(protein[3:5])  # inclusive:exclusive
# print(protein[0:6])  # again inclusive:exclusive

# print(protein.count('v'))
# print(str(protein.find('p')))  ## finds index num
# print(str(protein.find('kt'))) ## finds starting index num
# print(str(protein.find('w')))  ## yields -1 as 'w' is not present

#### Exercises ######
##Calculate AT content 
frag0 = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
frag0_length = len(frag0)
numA = frag0.count('A')
numT = frag0.count('T')
totalAT = numA + numT
proportionAT = totalAT/(frag0_length)
print('Proportion AT: ' + str(proportionAT))
print()

## Find complement of this DNA 
frag1 = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
a1 = frag1.replace('A', 't')
a2 = a1.replace('T', 'a')
a3 = a2.replace('G', 'c')
a4 = a3.replace('C', 'g')

print('The complement is ' + str(a4.upper()))
print()

## Restriction fragment lengths
frag2 = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
frag_length = len(frag2)
length1 = frag2.find('GAATTC') + 1
length2 = frag_length - length1

print('Total length: ' + str(frag_length))
print('Left length: ' + str(length1))
print('Right length: ' + str(length2))
print()

## Splicing out introns, pt 1
frag3 = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'
coding_region = frag3[62:90]
print('Non-coding region: ' + str(coding_region))
## Splicing out introns, pt 2
frag3_length = len(frag3)
cr_length = len(coding_region)
pct_coding = 100 * (cr_length/(frag3_length))
print('Total length frag3: ' + str(frag3_length))
print('Total length non-coding region: ' + str(cr_length))
print('Percent non-coding: ' + str(pct_coding))
print('Percent coding: ' + str(100 - pct_coding))
print()
## Splicing out introns, pt 3
print(frag3[0:62] + frag3[62:90].lower() + frag3[90:])
print()