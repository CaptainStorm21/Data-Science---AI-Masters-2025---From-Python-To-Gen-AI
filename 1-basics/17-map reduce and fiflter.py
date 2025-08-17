# Map Reduce Filter

import math


"""
Filter is a similar funciton but
it requires the function t look for a condition
ad then returns only those elements from the collections
that satisfies  the condition
"""

def area(r):
    return math.pi * (r ** 2)

radii = [1, 2, 3, 4, 5]

areas = list(map(area, radii))
# print(areas)

#### Map()
print('Map()')
result = list(map(area, radii))
print (result)

"""
Reduce - an operation that breaks down the entire
process into pairwise operations
and uses the result from each operation 
with the successive element
"""

