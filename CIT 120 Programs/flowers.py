# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input 
# file and prints the information to the user's screen. 
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file
with open('flowers.dat') as fp:
    
# Write while loop here
    lines = fp.readlines()
    for i in range(0,len(lines)-1,2):

# Print flower name using the following format
        flower = lines[i].split('.')[-1].replace('\n','')
        environment = lines[i+1].split('.')[-1].replace('\n','')

# print(var + " grows in the " + var2)
        print(flower + " grows in the " + environment)
