# loops
# Iterations  -> 
# Lists, Tuples, Strings, Dictionaries, Sets
# Loops For Loop, While Loop
# Iterating over a string

num_list = [1, 2, 3, 4, 5]
for num in num_list:
    print(num)
    
# Iterating over a tuple    
my_tuple = (10, 20, 30, 40)
for item in my_tuple:
    print(item) 
    
# Iterating over a string
my_string = "Welcome to Python!"
for char in my_string:
    print(char)
    
# Iterating over a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Iterating over a set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
    
# Using range() in a for loop
for i in range(5):
    print(i)    
    
# Using a while loop
count = 0
while count < 5:
    print(count)
    count += 1  
# Using a for loop with range()
for i in range(1, 6):
    print(i)        
# Using a for loop with a step
for i in range(0, 10, 2):
    print(i)    
# Using a for loop with a string
my_string = "Hello"     
for char in my_string:
    print(char)     
# Using a for loop with a list
my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print(num)
# Using a for loop with a tuple
my_tuple = (10, 20, 30, 40)
for item in my_tuple:
    print(item)
# Using a for loop with a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Using a for loop with a set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)     
# Using a while loop with a condition
count = 0
while count < 5:
    print(count)
    count += 1      
# Using a while loop with a break statement
count = 0
while True:
    if count >= 5:
        break   
    print(count)
    count += 1  
# Using a while loop with a continue statement
count = 0   
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest of the loop when count is 3
    print(count)
# Using a for loop with a list comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Using a for loop with a dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}  
# Using a for loop with a set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}
# Using a for loop with a string comprehension
vowels = "aeiou"
vowel_set = {char for char in vowels if char in 'aeiou'}
print(vowel_set)  # Output: {'a', 'e', 'i', 'o', 'u'}
# Using a for loop with a generator expression
squared_gen = (x**2 for x in range(5))
for num in squared_gen:
    print(num)          
    
x = 33
y = 44
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")    
    
if x % 2 == 0 and y % 2 == 0:
    print("Both x and y are even")
elif x % 2 == 0 or y % 2 == 0:
    print("At least one of x or y is even") 
elif x % 2 != 0 and y % 2 != 0:
    print("Both x and y are odd")
# Using a for loop with a string slice
my_string = "Hello, World! This is Thomas Jefferson."
print(my_string[0:5])   # Slice the string
print(my_string[10:20])   # Equivalent slice, omitting the start index
print(my_string[10:])  # Slice from index 10 to the end
print(my_string[:5])   # Slice from the start to index 5    


## Iterating over an list of integers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)   
# Iterating over a tuple of strings
fruits = ("apple", "banana", "cherry")  
for fruit in fruits:
    print(fruit)    
# Iterating over a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}   
for person, details in nested_dict.items():
    print(f"{person}: {details['name']} is {details['age']} years old")
# Iterating over a set of unique values
unique_numbers = {1, 2, 3, 4, 5}
for number in unique_numbers:
    print(number)

# Iterate throuhg a dictionary
employee = {
    1: {"name": "Alice Cooper", "position": "Engineer", "salary": 70000},
    2: {"name": "Bob Dylan", "position": "Manager", "salary": 80000},
    3: {"name": "Charlie Chaplin", "position": "Analyst", "salary": 60000}
}       
for emp_id, details in employee.items():
    print(f"Employee ID: {emp_id}, Name: {details['name']}, Position: {details['position']}, Salary: {details['salary']}")  
# Iterating over a string with a for loop

# Example: Print all employee names
for emp_id, details in employee.items():
    print(details['name'])  # This will print each employee's name
    
# Example: Print all employee occupations
for i,j in employee.items():
    print(j['position'])
    
# Example: Print all employee occupations
for i,j in employee.items():
    print(i)
    
# Example of interating through values in a dictionary
range_dict = {
    "a": 1,
    "b": 2, 
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6
}
for i in list(range_dict.keys())[3:5]:
    print(f"Range in the dictionary is {i}")
    # This will print the keys from index 3 to 5 in the dictionary
    
car_list = ["Toyota", "Honda", "Ford", "Chevrolet"]
car_list2 = []
# for i in car_list:
#    car_list2.append(i)
# print(car_list2)
car_list2 = [i for i in car_list]
print(car_list2)  # Output: ['Toyota', 'Honda', 'Ford', 'Chevrolet']

