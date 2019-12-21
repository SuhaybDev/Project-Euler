# Program to find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9


# Importing permutations from itertools module
from itertools import permutations

# Function converter(tup) takes all the elements of a tuple and joins them into a string
def converter(tup): 
    str =  ''.join(tup) 
    return str

# Assinging all the permutations of the digits to perm
perm = permutations('0123456789')

# Assingning 0 to variable x
x = 0


# Iterating through the permutations of the given digits
for i in perm:
    # Adding 1 to x whenever a permutation is found
    x += 1
    # If statement for when x hits 1,000,000
    if x == 1000000:
        # Converting the found permutation from tuple to string
        final_perm = converter(i)
        # Printing the millionth lexicographic permutation
        print(final_perm)


# Note: Since permutations() outputs values in lexicographic order there is no need for further sorting