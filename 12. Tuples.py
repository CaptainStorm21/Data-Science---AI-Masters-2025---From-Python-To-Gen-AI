# tuples
# Tuples are immutable sequences in Python, used to store multiple items in a single variable.  
# They are defined by enclosing the items in parentheses.   
# Example of creating a tuple
my_tuple = (1, 2, 3, 4, 5)
# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2
# Tuples can contain mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)  # Output: (1, 'Hello', 3.14, True)          
# Tuples can also be nested
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple)  # Output: (1, (2, 3), (4, 5))
# Tuples support various operations like concatenation and repetition
tuple1 = (1, 2) 
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4)       
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)