'''
Program to find the number of all possiple routes starting in the top left corner of a 20×20 grid
and only being able to move to the right and down to reach the bottom right corner.
'''

from functools import lru_cache


# Function to find all the possible routes and caching values to improve runtime
@lru_cache()
def paths(x, y):
    if x == 1:
        return 1
    elif y == 1:
        return 1
    else:
        return paths(x-1,y) + paths(x,y-1)


# Printing the number of found routes
print(paths(21,21))








