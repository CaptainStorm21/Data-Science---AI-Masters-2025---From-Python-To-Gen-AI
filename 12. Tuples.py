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
# t4 = ('Hello', 2, 3.14)
# print(len(t4)) # Output: 3
# nested_tuple = (1, 2, 3, (4, 5))
# print(len(nested_tuple))  # Output: 4   
# # Tuples can be unpacked into variables
# var = t4[0]
# print(var) # Output: Hello

# # how to access nested tuple inside of a tuple
# nested_tuple = (1, 2, (3, 4), 5)
# nested_element = nested_tuple[2][1] # Accessing the second element of the nested tuple
# print(nested_element)  # Output: 4  

# type of tuples
# my_tuple = (1,)
# my_tuple2 = (100)
# my_tuple3 = 200
# print(type(my_tuple))  # Output: <class 'tuple'>
# print(type(my_tuple2))  # Output: <class 'int'> (not a tuple, just an integer)
# print(type(my_tuple3))

# indexing in tuples        
# my_tuple = (10, 20, 30, 40, 50, "London", "Hiroshima")
# print (len(my_tuple))   # Output: 5
# print(my_tuple[0])  # Output: 10
# print(my_tuple[3])  # Output: 40
# # print last 2 fron my tuple
# print(my_tuple[3:4])  # Output: 50      
# print(my_tuple[-1])  # Output: London
# print(my_tuple[-2])  # Output: 50

hiroshima = ("Hello Hiroshima Flow",)  # This is a tuple containing a string
my_string = hiroshima[0]  # Access the string element from the tuple

hiroshima_sliced = my_string[3:7]  # Slice the string
print("printing sliced string:")
print(hiroshima_sliced)  # Expected Output: lo Hiro

print(my_string[0:5])  # Slice the string
print(my_string[10:20])   #  Equivalent slice, omitting the start index
print(my_string[10:])  # Slice from index 10 to the end
print(my_string[:5])

t = (10, 20, 30, 40, 50)
print(t[1:4])    # Output: (20, 30, 40)
print(t[:3])     # Output: (10, 20, 30)
print(t[::2])    # Output: (10, 30, 50)

# Concatenating tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 6)

# Mathematical operations on tuples
t4 = (10, 20, 30, 89)
print(t4[0] + t4[1]) # Output: 30
print(sum(t4))  # Output: 60 (sum of all elements in the tuple)

# Adding elements in mixex tuples
mixed_tuple = (2, 4, 71, 332, "Hello", "los angeles", True, 2123.22)
original_numbers = [item for item in mixed_tuple if isinstance(item, (int, float))]
int_numbers = [item for item in original_numbers if isinstance(item, int)]
float_numbers = [item for item in original_numbers if isinstance(item, float)]


# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
nested_element = nested_tuple[2][1] # Accessing the second element of the nested tuple
print(nested_element)  # Output: 4
# Accessing elements in a nested tuple
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[2][0])  # Output: 3
print(nested_tuple[2][1])  # Output: 4      
# Accessing elements in a nested tuple
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[2][0])  # Output: 3

# tuple immutability
# Tuples are immutable, meaning once created, they cannot be modified.
# This means you cannot add, remove, or change elements in a tuple. 
# However, you can create a new tuple based on an existing one.
# Example of creating a new tuple from an existing one

list_countries = ["USA", "Canada", "Mexico"]
tuple_countries = tuple(list_countries)
print(tuple_countries)  # Output: ('USA', 'Canada', 'Mexico')   
# list_countries[3] = "UK"
# print(tuple_countries)  
# This will raise an error because tuples are immutable   
list_countries[0:2] = ["UK", "Germany"]
tuple_countries = tuple(list_countries)
print(tuple_countries)  # Output: ('UK', 'Germany', 'Mexico')
new_countries = tuple_countries + ("France", "Spain", "Italy", "Japan", "China")
print(new_countries)  # Output: ('UK', 'Germany', 'Mexico', 'France', 'Spain', 'Italy', 'Japan', 'China')

