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
print(nested_list[1][2])  # Notre-Dame Cathedral
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

# List Concat
list_cities = ["New York", "Los Angeles", "Chicago"]
list_countries = ["USA", "USA", "USA"]
combined_list = list_cities + list_countries
print(combined_list)  
# Combined list of cities and countries 
# Repeating lists
repeated_cities = list_cities * 2
print(repeated_cities)  # Print the repeated list of cities     
# Checking if a list is empty
is_empty_cities = len(list_cities) == 0
print(is_empty_cities)  # False, since list_cities has elements     
# Length of the combined list
print(len(combined_list))   # Type of the combined list
print(type(combined_list))  # <class 'list'>, since combined_list is a list
# Accessing elements in the combined list
print(combined_list[0])  # First element        
print(combined_list[3])  # Fourth element
# Slicing the combined list
print(combined_list[1:4])  # Elements from index 1 to 3 
# Reversing the combined list
combined_list.reverse()
print(combined_list)  # Print the reversed combined list
# Sorting the combined list
combined_list.sort()
print(combined_list)  # Print the sorted combined list
# Nested list example
nested_combined_list = [["New York", "Los Angeles"], ["USA", "USA"]]
print("New York" in nested_combined_list[0])  # True, since "New York" is in the first sublist
# Accessing elements in the nested combined list
print(nested_combined_list[0][1])  # Los Angeles

# Adding a new city to the nested combined list
nested_combined_list[0].append("Chicago")
print(nested_combined_list[0])  # Print the updated first sublist               
# Removing a city from the nested combined list 

nested_combined_list[0].remove("Los Angeles")
print(nested_combined_list[0])  # Print the updated first sublist after removal
# Checking if a city exists in the nested combined list
print("Chicago" in nested_combined_list[0])  # True, since "Chicago" is in the first sublist        
# Length of the nested combined list
print(len(nested_combined_list[0]))  # Number of cities in the first sublist
# Copying the nested combined list
copied_nested_combined_list = nested_combined_list.copy()
print(copied_nested_combined_list)  # Print the copied nested combined list     
# Clearing the combined list
combined_list.clear()
print(combined_list)  # Should print an empty list after clearing
# Concatenating two lists
list_a = ["apple", "banana", "cherry"]
list_b = ["date", "elderberry", "fig"]
concatenated_fruits = list_a + list_b
print(concatenated_fruits)
# Repeating the concatenated list
repeated_fruits = concatenated_fruits * 2
print(repeated_fruits)      
# Checking if the concatenated list is empty

# extend() method to add multiple elements
gems1 = ["diamond", "ruby"]
gems2 = ["sapphire", "emerald"]
gems1.extend(gems2)
print(gems1)  # ['diamond', 'ruby', 'sapphire', 'emerald']
# Using the insert() method to add an element at a specific position
gems1.insert(2, "topaz")
print(gems1)  # ['diamond', 'ruby', 'topaz', 'sapphire', 'emerald']
# Using the pop() method to remove and return the last element
last_gem = gems1.pop()  
print(last_gem)  # 'emerald'
print(gems1)  # ['diamond', 'ruby', 'topaz', 'sapphire']
# Using the index() method to find the index of an element
index_of_ruby = gems1.index("ruby")
print(index_of_ruby)  # 1
# Using the count() method to count occurrences of an element
count_of_topaz = gems1.count("topaz")
print(count_of_topaz)
# 1, since "topaz" appears once in the list
# Using the clear() method to remove all elements from the list
gems1.clear()
print(gems1)  # Should print an empty list

#What is append?
#If you are doing list one equals to this list one dot, append this.
#That means this total entity five comma six is appended to the list as a new element.
# So the list one is going to be a list of five elements.
# If you are doing list one equals to this list one dot append this, that means this total entity five comma six is appended to the list as a new element.  
#So the new element, the fifth element is going to be a list.
phone_list = ["iPhone", "Samsung", "Google Pixel"]
# Adding a new phone to the list
phone_list.append("OnePlus")
print(phone_list)  # ['iPhone', 'Samsung', 'Google Pixel', 'OnePlus']   

phone_list.append([
    "Nokia", "Samsung SK23"])
print(phone_list) 