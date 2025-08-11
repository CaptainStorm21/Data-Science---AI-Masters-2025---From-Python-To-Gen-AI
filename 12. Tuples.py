# tuples
# Tuples are immutable sequences in Python, used to store multiple items in a single variable.  
# They are defined by enclosing the items in parentheses.   
# Triples are ordered collections, meaning the items have a defined order and can be accessed by their index.
# Tuples can contain any data type, including numbers, strings, and even other tuples.
# They are often used to group related data together, and since they are immutable, they can be used as keys in dictionaries.
# Example of creating a tuple
# my_tuple = (1, 2, 3, 4, 5)
# # Accessing elements in a tuple
# print(my_tuple[0])  # Output: 1
# print(my_tuple[1])  # Output: 2
# # Tuples can contain mixed data types
# mixed_tuple = (1, "Hello", 3.14, True)
# print(mixed_tuple)  # Output: (1, 'Hello', 3.14, True)          
# # Tuples can also be nested
# nested_tuple = (1, (2, 3), (4, 5))
# print(nested_tuple)  # Output: (1, (2, 3), (4, 5))
# # Tuples support various operations like concatenation and repetition
# tuple1 = (1, 2) 
# tuple2 = (3, 4)
# concatenated_tuple = tuple1 + tuple2
# print(concatenated_tuple)  # Output: (1, 2, 3, 4)       
# repeated_tuple = tuple1 * 3
# print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)


# tuples are immutable, meaning once created, they cannot be modified
# This means you cannot add, remove, or change elements in a tuple.
# However, you can create a new tuple based on an existing one.
# Example of creating a new tuple from an existing one

# t = (1, 2, 3)
# t2 =(32, 4, 5)
# new_tuple = t + t2
# type(new_tuple)  # Output: <class 'tuple'>
# type(t2)
t4 = ('Hello', 2, 3.14)
print(len(t4)) # Output: 3
nested_tuple = (1, 2, 3, (4, 5))
print(len(nested_tuple))  # Output: 4   
# Tuples can be unpacked into variables
var = t4[0]
print(var) # Output: Hello

# how to access nested tuple inside of a tuple
nested_tuple = (1, 2, (3, 4), 5)
nested_element = nested_tuple[2][1] # Accessing the second element of the nested tuple
print(nested_element)  # Output: 4  