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

# del command to delete an element from the list

delete_list = [
    "apple", 
    "banana", 
    "cherry", 
    "date"]
# Deleting the second element (index 1)
del delete_list[1]
print(delete_list)  # ['apple', 'cherry', 'date']
# Deleting the entire list
del delete_list
# print(delete_list)  # This will raise an error since delete_list no longer exists 
# Using the pop() method to remove and return the last element
pop_list = ["apple", "banana", "cherry"]
last_fruit = pop_list.pop()  
print(last_fruit)  # 'cherry'
print(pop_list)  # ['apple', 'banana']  
# Using the pop() method to remove and return an element at a specific index
second_fruit = pop_list.pop(1)  
print(second_fruit)  # 'banana'
print(pop_list)  # ['apple']    
# Using the index() method to find the index of an element
index_list = ["apple", "banana", "cherry"]
index_of_banana = index_list.index("banana")    
print(index_of_banana)  # 1
# Using the count() method to count occurrences of an element
count_list = ["apple", "banana", "cherry", "banana"]    
count_of_banana = count_list.count("banana")
print(count_of_banana)
# 2, since "banana" appears twice in the list

# pop() vs remove()
# pop() removes an element at a specific index and returns it, while remove() removes the first occurrence of a specified value.
# Example of pop()
example_list = ["apple", "banana", "cherry"]
removed_item = example_list.pop(1)  # Removes "banana"
print(removed_item)  # 'banana'
print(example_list)  # ['apple', 'cherry']
# Example of remove()
example_list.remove("apple")  # Removes the first occurrence of "apple"
print(example_list)  # ['cherry']   
# Using the clear() method to remove all elements from the list
clear_list = ["apple", "banana", "cherry"]
clear_list.clear()
print(clear_list)  # Should print an empty list
# Using the copy() method to create a shallow copy of the list
copy_list = ["apple", "banana", "cherry"]
shallow_copy = copy_list.copy()
print(shallow_copy) # ['apple', 'banana', 'cherry'] 
# Modifying the original list does not affect the copy

# sort()
# Using the sort() method to sort the list in ascending order   
sort_list = ["banana", "apple", "cherry"]
sort_list.sort()
print(sort_list)  # ['apple', 'banana', 'cherry']
# Using the sort() method with reverse=True to sort in descending order
sort_list.sort(reverse=True)    
print(sort_list)  # ['cherry', 'banana', 'apple']   
# Using the sorted() function to return a new sorted list without modifying the original
original_list = ["banana", "apple", "cherry"]
sorted_list = sorted(original_list)
print(sorted_list)  # ['apple', 'banana', 'cherry']
# The original list remains unchanged
print(original_list)    
# ['banana', 'apple', 'cherry']
# Using the sorted() function with reverse=True to return a new sorted list in descending order
sorted_list_desc = sorted(original_list, reverse=True)
print(sorted_list_desc)  # ['cherry', 'banana', 'apple']
# The original list remains unchanged
print(original_list)  # ['banana', 'apple', 'cherry']           
# Using the reverse() method to reverse the order of the list
reverse_list = ["banana", "apple", "cherry"]
reverse_list.reverse()
print(reverse_list) # ['cherry', 'apple', 'banana']     
# Using the reversed() function to return an iterator that yields the elements of the list in reverse order
reversed_list = list(reversed(reverse_list))
print(reversed_list)  # ['banana', 'apple', 'cherry']       
# The original list remains unchanged
print(reverse_list)  # ['cherry', 'apple', 'banana']
    # Using the join() method to concatenate elements of a list into a string
join_list = ["apple", "banana", "cherry"]
joined_string = ", ".join(join_list)
print(joined_string)  # 'apple, banana, cherry' 
# Using the split() method to split a string into a list
split_string = "apple, banana, cherry"
split_list = split_string.split(", ")
print(split_list)   
# ['apple', 'banana', 'cherry']
# Using the zip() function to combine two lists into a list of tuples
list1 = [1, 2, 3]       

list2 = ["a", "b", "c"]
zipped_list = list(zip(list1, list2))
print(zipped_list)  # [(1, 'a'), (2, 'b'), (3, 'c')]
# Using the enumerate() function to get an index and value for each element in a list
enumerated_list = list(enumerate(join_list))
print(enumerated_list)  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# Using the map() function to apply a function to each element in a list
squared_list = list(map(lambda x: x**2, list1)) 
print(squared_list)  # [1, 4, 9]                
# Using the filter() function to filter elements in a list based on a condition
filtered_list = list(filter(lambda x: x > 1, list1))
print(filtered_list)        
# [2, 3]        
# Using the reduce() function from functools to apply a function cumulatively to the items of a list
from functools import reduce
sum_list = reduce(lambda x, y: x + y, list1)
print(sum_list)  # 6    
# Using the any() function to check if any element in a list is True
any_list = [False, True, False]
print(any(any_list))  # True, since there is at least one True element      
# Using the all() function to check if all elements in a list are True
all_list = [True, True, True]
print(all(all_list))        # True, since all elements are True
# Using the max() function to find the maximum element in a list
max_list = [1, 2, 3, 4, 5]
print(max(max_list))                        
# 5, since 5 is the maximum element in the list
# Using the min() function to find the minimum element in a list
min_list = [1, 2, 3, 4, 5]
print(min(min_list))  # 1, since 1 is the minimum element in the list
# Using the sum() function to calculate the sum of elements in a list
sum_list = [1, 2, 3, 4, 5]
print(sum(sum_list))  # 15, since the sum of elements is 15

# sort() vs sorted()
# sort() modifies the original list in place, while sorted() returns a new sorted list without modifying the original.
# Example of sort()     
example_sort = [3, 1, 2]
example_sort.sort()
print(example_sort)  # [1, 2, 3]
# Example of sorted()
example_sorted = [3, 1, 2]
new_sorted = sorted(example_sorted)
print(new_sorted)  # [1, 2, 3]
print(example_sorted)  # [3, 1, 2], original list remains unchanged
# Using the reverse() method to reverse the order of the list
reverse_example = [3, 1, 2]
reverse_example.reverse()
print(reverse_example)  # [2, 1, 3]
# Using the reversed() function to return an iterator that yields the elements of the list in reverse order
reversed_example = list(reversed(reverse_example))
print(reversed_example) # [3, 1, 2], original list remains unchanged
# Using the join() method to concatenate elements of a list into a string
join_example = ["apple", "banana", "cherry"]
joined_string_example = ", ".join(join_example)
print(joined_string_example)
# 'apple, banana, cherry'
# Using the split() method to split a string into a list
split_example = "apple, banana, cherry"     
split_list_example = split_example.split(", ")
print(split_list_example)  # ['apple', 'banana', 'cherry']

# shadow copy vs deep copy
# Shadow copy creates a new reference to the same object, while deep copy creates a new object with a copy of the original object's data.
# Example of shadow copy        
shadow_copy = [1, 2, 3]
shadow_copy_ref = shadow_copy  # This creates a new reference to the same list
shadow_copy_ref.append(4)
print(shadow_copy)  # [1, 2, 3, 4], both references point to the same list              
# Example of deep copy
import copy
deep_copy = [1, 2, 3]
deep_copy_ref = copy.deepcopy(deep_copy)        
deep_copy_ref.append(4)     
print(deep_copy)  # [1, 2, 3], original list remains unchanged
print(deep_copy_ref)  # [1, 2, 3, 4], deep copy has its own separate data       
# Using the copy() method to create a shallow copy of the list  
shallow_copy_example = ["apple", "banana", "cherry"]
shallow_copy_ref_example = shallow_copy_example.copy()
print(shallow_copy_ref_example) 
# ['apple', 'banana', 'cherry'] 
# Modifying the original list does not affect the copy
shallow_copy_example.append("date")
print(shallow_copy_example)             
# ['apple', 'banana', 'cherry', 'date']
print(shallow_copy_ref_example) # ['apple', 'banana', 'cherry'] 
# Using the copy() method to create a shallow copy of a nested list