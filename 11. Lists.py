# Lists are modifyable sequences in Python that can hold a collection of items.
numbers = [1, 2, 3, 4, 5]
print(numbers)  

# Adding an element to the list
numbers.append(6)
print(numbers)  
# Removing an element from the list
numbers.remove(3)
print(numbers)  
# Accessing elements in the list
print(numbers[0])  # First element
print(numbers[-1])  # Last element      
# Slicing the list
print(numbers[1:4])
# Reversing the list
numbers.reverse()
print(numbers)
# Sorting the list
numbers.sort()
print(numbers)

list1 = [1, 2, 3, "a", "b", "c"]
list1.append("d")
print(list1)
# Checking if an item exists in the list    
print("a" in list1)  # True
print("x" in list1)  # False    
# Length of the list
print(len(list1))  # 7
# Nested lists
nested_list = [1, 2, [3, 4, 5], 6]
print(nested_list[2])   # Accessing an element in the nested list
print(nested_list[2][1])  # Accessing an element in the nested list
# List comprehension
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  
# List comprehension with condition
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# Copying a list
copied_list = numbers.copy()    
print(copied_list)
# Clearing a list
numbers.clear()
print(numbers)  # Should print an empty list
# Concatenating lists
list2 = [7, 8, 9]
concatenated_list = list1 + list2
print(concatenated_list)    
# Repeating lists
repeated_list = list1 * 2
print(repeated_list)   

print(len(list1))  # Length of list1
print(type(list1))  # Type of list1
# Checking if a list is empty
is_empty = len(list1) == 0
print(is_empty)  # False, since list1 has elements

customer_info = ["Alice", 30, "Engineer", 1300.50, "1GB", "Milan", "Italy"]# This will return <class 'list'>p
# why is it false
print(len(customer_info)) 
# Accessing elements in the customer_info list
print(customer_info) 
# Accessing specific elements
print(customer_info[0])
print(customer_info[1])  # Age
print(customer_info[2])  # Occupation
print(customer_info[3])  # Salary
print(customer_info[4])  # Data plan
print(customer_info[5])  # City
print(customer_info[6])  # Country  
# Modifying an element in the list
customer_info[1] = 31       
print(customer_info)  # Updated age
# Adding a new element to the list
customer_info.append("New York")   
print(customer_info)             

# nested list example
nested_list = []
nested_list = [ "France", "Paris", 48.8566, 2.3522, ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"] ]
print(nested_list)  # Print the entire nested list
# Accessing elements in the nested list
print(nested_list[0])  # Country        
print(nested_list[-1][2])  # Notre-Dame Cathedral
# Adding a new attraction to the nested list
nested_list[-1].append("Montmartre")
print(nested_list[-1])  # Print the updated attractions list
# Removing an attraction from the nested list
nested_list[-1].remove("Louvre Museum")     
print(nested_list[-1])  # Print the updated attractions list after removal
# Checking if an attraction exists in the nested list
print("Eiffel Tower" in nested_list[-1])  # True
# Length of the nested list
print(len(nested_list[-1]))  # Number of attractions
# Copying the nested list
copied_nested_list = nested_list.copy()                 
print(copied_nested_list)  # Print the copied nested list