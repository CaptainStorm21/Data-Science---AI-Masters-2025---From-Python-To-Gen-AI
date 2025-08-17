# Map Reduce Filter

import math


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




"""
Reduce - an operation that breaks down the entire
process into pairwise operations
and uses the result from each operation 
with the successive element
"""

