# Dictionary
# A dictionary is a collection of key-value pairs.
# Each key is unique and is used to access its corresponding value.         

# Dictionaries are mutable, meaning you can change their content after creation.
# Example of creating a dictionary

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "zip_code": "10001"
    },  
    "grades": (90, 85, 88)  # Tuples can also be used as values
}

# Accessing values in a dictionary using keys
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])  # Output: 30
print(my_dict["city"])  # Output: New York
print(my_dict["is_student"])  # Output: False
print(my_dict["courses"])  # Output: ['Math', 'Science', 'History']
print(my_dict["address"]["street"])

# Adding a new key-value pair to the dictionary
my_dict["email"] = "nowhere@yahoo.com"
print(my_dict["email"])  
# Output:nowhere@yahoo.com
# Modifying an existing value in the dictionary
my_dict["age"] = 31
print(my_dict["age"])  # Output: 31 
# Removing a key-value pair from the dictionary
del my_dict["is_student"]
print(my_dict)  
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'courses': ['Math', 'Science', 'History'], 'address': {'street': '123 Main St', 'zip_code': '10001'}, 'grades': (90, 85, 88), 'email': ' 
print(len(my_dict))     
# Output: 7 (number of key-value pairs in the dictionary)
# Checking if a key exists in the dictionary
if "name" in my_dict:
    print("Name exists in the dictionary")
else:
    print("Name does not exist in the dictionary")
# Output: Name exists in the dictionary
# Iterating over keys in the dictionary
for key in my_dict:
    print(key)
# Output: name, age, city, courses, address, grades, email

print(my_dict.values())  
# Returns a view object containing all the values in the dictionary
print(my_dict.keys()) 
# Returns a view object containing all the keys in the dictionary
print(my_dict.items())  
# Returns a view object containing all the key-value pairs in the dictionary    
print(my_dict.get("name"))  # Accessing value using get method
# Output: Alice
print(my_dict.get("non_existent_key", "Default Value"))  
# Output: Default Value (returns default value if key does not exist)   
my_dict.update({"name": "Alce Sholtz"})  
print(my_dict["name"])  # Output: Alce Sholtz
print(my_dict)

my_employee = {
    1: {
        "name": "John Doe",
        "position": "Software Engineer",
        "salary": 75000,
        "skills": ["Python", "JavaScript", "SQL"],
        "is_full_time": True,
        "address": {
            "street": "456 Elm St",
            "city": "San Francisco",
            "zip_code": "94101"
        }
    },
    2: {
        "name": "Jane Smith",
        "position": "Data Scientist",   
        "salary": 85000,
        "skills": ["Python", "Machine Learning", "Data Visualization"],
        "is_full_time": True,
        "address": {
            "street": "789 Oak St",
            "city": "Los Angeles",
            "zip_code": "90001"
        }
    },
    4: {
        "name": "Bob Johnson",
        "position": "DevOps Engineer",  
        "salary": 80000,    
        "skills": ["Docker", "Kubernetes", "CI/CD"],
        "is_full_time": True,
        "address": {
            "street": "123 Maple St",
            "city": "Chicago",
            "zip_code": "60601"
        }
    }               
 }


# Accessing nested dictionary values
print(my_employee[1]["name"])  
# Output: John Doe
print(my_employee[1]["position"]) 
# Output: Software Engineer
for employee_id, employee_data in my_employee.items():
    print(employee_data["name"])
# Output: John Doe, Jane Smith
# Adding a new employee
my_employee[3] = {
    "name": "Alice Johnson",
    "position": "Product Manager",      
    "salary": 95000,
    "skills": ["Product Management", "Agile", "Leadership"],
    "is_full_time": True,
    "address": {        
        "street": "321 Pine St",
        "city": "Seattle",  
        "zip_code": "98101"
    }   
}
print(len(my_employee))

# Removing an employee
del my_employee[2]
print(my_employee)

# getting an employee by ID
print(my_employee.get(1))
# Output: {'name': 'John Doe', 'position': 'Software Engineer', 'salary': 75000, 'skills': ['Python', 'JavaScript', 'SQL'], 'is_full_time': True, 'address': {'street': '456 Elm St', 'city': 'San Francisco', 'zip_code': '94101'}}    
print(type(my_employee.get(1)))

johns_data = my_employee[1]
print(johns_data)

# Access John's name directly
johns_name = my_employee[1]["name"]
print(johns_name)

# get all the values of John's data
print(list(my_employee.values()))
# Output: [{'name': 'John Doe', 'position': 'Software Engineer', 'salary': 75000, 'skills': ['Python', 'JavaScript', 'SQL'], 'is_full_time': True, 'address': {'street': '456 Elm St', 'city': 'San Francisco', 'zip_code': '94101'}}, {'name': 'Alice Johnson', 'position': 'Product Manager', 'salary': 95000, 'skills': ['Product Management', 'Agile', 'Leadership'], 'is_full_time': True, 'address': {'street': '321 Pine St', 'city': 'Seattle', 'zip_code': '98101'}}]
# get all the keys of John's data

print(list(my_employee[1].keys()))

album_dict = {
    "rock": "The Dark Side of the Moon",
    "rap": "The Marshall Mathers LP",
    "pop": "Thriller",
    "jazz": "Kind of Blue",
    "classical": "Symphony No. 5",
    "country": "The Essential Johnny Cash",
    "electronic": "Discovery",  
    "blues": "Live at the Regal",
    "reggae": "Legend",
    "metal": "Dark Passion Play",
    "folk": "The Freewheelin' Bob Dylan",
    "hip_hop": "To Pimp a Butterfly"  
}
# Accessing values in the album dictionary
print(album_dict["rock"])  # Output: The Dark Side of the Moon
print(album_dict["rap"])  # Output: The Marshall Mathers LP

sorted_albums = sorted(album_dict.items(), key=lambda x: x[1])
print(sorted_albums)  
# Output: [('blues', 'Live at the Regal'), ('classical', 'Symphony No. 5'), ('country', 'The Essential Johnny Cash'), ('electronic', 'Discovery'), ('folk', "The Freewheelin' Bob Dylan"), ('hip_hop', 'To Pimp a Butterfly'), ('jazz', 'Kind of Blue'), ('metal', 'Dark Passion Play'), ('pop', 'Thriller'), ('rap', 'The Marshall Mathers LP'), ('reggae', 'Legend'), ('rock', 'The Dark Side of the Moon')]

# Sorting the dictionary by keys
sorted_album_keys = sorted(album_dict.keys())
print(sorted_album_keys)
# Output: ['blues', 'classical', 'country', 'electronic', 'folk', 'hip_hop', 'jazz', 'metal', 'pop', 'rap', 'reggae', 'rock']
# Sorting the dictionary by values
sorted_album_values = sorted(album_dict.values())
print(sorted_album_values)
# Output: ['Dark Passion Play', 'Discovery', 'Kind of Blue', 'Live at the Regal', 'Legend', 'Symphony No. 5', 'The Dark Side of the Moon', 'The Essential Johnny Cash', 'The Freewheelin' Bob Dylan', 'The Marshall Mathers LP', 'Thriller', 'To Pimp a Butterfly']

# Converting a dictionary to a list of tuples
dict_items = list(album_dict.items())   

print(dict_items)
# Output: [('rock', 'The Dark Side of the Moon'), ('rap', 'The Marshall Mathers LP'), ('pop', 'Thriller'), ('jazz', 'Kind of Blue'), ('classical', 'Symphony No. 5'), ('country', 'The Essential Johnny Cash'), ('electronic', 'Discovery'), ('blues', 'Live at the Regal'), ('reggae', 'Legend'), ('metal', 'Dark Passion Play'), ('folk', "The Freewheelin' Bob Dylan"), ('hip_hop', 'To Pimp a Butterfly')]
# Converting a list of tuples to a dictionary
list_of_tuples = [('rock', 'The Dark Side of the Moon'), ('rap', 'The Marshall Mathers LP')]
new_album_dict = dict(list_of_tuples)
print(new_album_dict)  
# Output: {'rock': 'The Dark Side of the Moon', 'rap': 'The Marshall Mathers LP'}
