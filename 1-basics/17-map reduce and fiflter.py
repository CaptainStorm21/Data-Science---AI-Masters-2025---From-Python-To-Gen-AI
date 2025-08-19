# Map Reduce Filter

import math
import statistics
from functools import reduce


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
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# List of cities with their temperatures in Celsius
cities = [{
    "Oulu": 0, 
    "Cairo": 20, 
    "Dubai": 100, 
    "South Pole": -10, 
    "Durban": 37, 
    "Sahara": 25
}]

# Convert the dictionary to a list of tuples: (city, temperature)
city_temp_pairs = list(cities[0].items())

# Filter cities with temperatures above 0°C
filtered_cities = filter(lambda x: x[1] > 0, city_temp_pairs)

# Convert the filtered cities' temperatures to Fahrenheit
result = {city: celsius_to_fahrenheit(temp) for city, temp in filtered_cities}

print(result)

# Flatten the list of dictionaries into a list of (city, temperature) tuples
city_temp_pairs = [(list(city.keys())[0], list(city.values())[0]) for city in cities]

# Filter cities with temperatures above 0°C
filtered_cities = filter(lambda x: x[1] > 0, city_temp_pairs)

# Convert the filtered cities' temperatures to Fahrenheit
result_flat = {city: celsius_to_fahrenheit(temp) for city, temp in filtered_cities}

# Print the result vertically
print("Cities with temperatures above 0°C in Fahrenheit:")
for city, temp in result_flat.items():
    print(f"{city}: {temp:.1f}°F")

# Using map
# Lambda function to convert Celsius to Fahrenheit
cel_to_f = lambda data: (data[0], (9/5)*data[1]+32)

# List of tuples (city, temperature) in Celsius
temps = [("Oulu", 0), ("Cairo", 20), ("Dubai", 100), ("South Pole", -10)]

# Apply the lambda function to each tuple in temps using map
filtered_map_cities = map(cel_to_f, temps)

# Convert the result to a list and print
print(list(filtered_map_cities))

"""
Reduce - an operation that breaks down the entire
process into pairwise operations
and uses the result from each operation 
with the successive element
"""

cars = [
    ("Toyota Camry", 2012, 18000),
    ("Honda Accord", 2018, 25000),
    ("Tesla Model 3", 2021, 35000),
    ("Ford Fiesta", 2015, 15000),
    ("BMW 3 Series", 2019, 45000),
    ("Chevrolet Malibu", 2016, 22000)
]

# Filter cars that are newer than 2015 and cost more than $20,000
filtered_cars = filter(lambda car: car[1] > 2015 and car[2] > 20000, cars)

# Convert the result to a list and print
filtered_cars_list = list(filtered_cars)
print(filtered_cars_list)

# List of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Calculate the mean (average) of the list
mean_value = statistics.mean(numbers)
print(mean_value)

# Filter out numbers that are above the mean
filtered_numbers = filter(lambda x: x > mean_value, numbers)

# Convert the result to a list and print
filtered_numbers_list = list(filtered_numbers)
print("Numbers above the mean:", filtered_numbers_list)

# Getting rid of Null / NaN values
names = ["Alex", "Mary", 0, 0.00, "Valeria", ""]
filter(None, names)
print (list(filter(None, names)))

nums = [21, 33, 22.3, 0, 0.00, "", 0]
filter(None, nums)
print (list(filter(None, nums)))

# reduce
nums_data = [1, 2, 3, 4, 5]
multiplier = lambda x, y:x*y 
print(reduce(multiplier, nums_data))

prev = nums_data[0]
for i in nums_data[1:]:
    prev = prev * i
print(prev)

prev = nums_data[0]
for i in nums_data:
    i = i * prev
    prev = i
print(prev)

# Multiply all the items in a list
multi_data2 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, multi_data2)
print(result)
