# Sets
# Unordered collection of unique elements.
# Sets are mutable, but the elements must be immutable (like numbers, strings, or tuples).
# They are useful for membership testing, removing duplicates from a sequence, and performing mathematical set operations like union, intersection, and difference.     
# Sets can be created using curly braces `{}` or the `set()` constructor.       

# we use sets when we want to store a collection of unique items and perform operations like union, intersection, and difference.
# Example of creating a set
# Or convert the set to a string first
colors = {"red", "green", "blue"}
print(colors)  # Output: {'red', 'green', 'blue', 'blue'}
print(f"Example of sets: {colors}")
print("Example of sets: " + str(colors))


# uniques# Example of creating a set
my_set = {1, 2, 3, 4, 5, 323, 5, 5, 5, 5, 23432, 234, 234, 234, 234, 234, 234, 234, 234, 234}
print(my_set)  # Output: {1, 2, 3, 4, 5, 323, 23432, 234}  
# Sets can contain mixed data types
mixed_set = {1, "Hello", 3.14, True}
print(len(my_set))  # Output: 10 (duplicates are removed) 
# Sets do not support indexing or slicing like lists or tuples, as they are unordered.
# However, you can check for membership using the `in` keyword.
print(1 in my_set)  # Output: True
print(6 in my_set)  # Output: False  
print(mixed_set) 
# Output: {1, 'Hello', 3.14} (True is treated as 1, so it doesn't duplicate)  
my_set_2 = set(my_set)
print(my_set_2)  # Output: {1, 2, 3, 4, 5, 323, 23432, 234} 

my_cities = {"London", "Hiroshima", "Tokyo", "New York"}
print(my_cities)  # Output: {'London', 'Hiroshima', 'Tokyo', 'New York'}    
# Adding elements to a set
my_cities.add('New Orleans')
print(my_cities) 

# set operations
# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5} 
# Intersection
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
# Difference
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
# Removing elements from a set
my_cities.remove('Tokyo')
print(my_cities)                
# Output: {'London', 'Hiroshima', 'New York', 'New Orleans'}
# Note: If you try to remove an element that doesn't exist, it will raise a KeyError.
# To avoid this, you can use `discard()` which does not raise an error if the element is not found.
my_cities.discard('Tokyo')  # No error, even though 'Tokyo' is already removed
print(my_cities)  # Output: {'London', 'Hiroshima', 'New York', 'New Orleans'}  
# Clearing a set
my_cities.clear()
print(my_cities)  # Output: set() (empty set)
# Copying a set
my_cities_copy = my_cities.copy()
print(my_cities_copy)  # Output: set() (copy of the empty set)  

# 
A = {3, 5, 7, 9, 11, 13, 21, 23, 25, 27 }
B = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
# Union
print(A | B)  
# Output: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27} 
# Intersection  
print(A & B)
# Output: {3, 5, 7, 9, 11, 13}  
# Difference
print(A - B)
# Output: {21, 23, 25, 27}  
# Symmetric Difference
print(A ^ B)
# Output: {1, 15, 17, 19, 21, 23, 25, 27}   
# Membership testing
print(3 in A)  # Output: True
print(4 in A)  # Output: False
# Length of a set
print(len(A))  # Output: 10
# Iterating through a set
for item in A:
    print(item, end=' ')    # Output: 3 5 7 9 11 13 21 23 25 27
# Converting a list to a set to remove duplicates