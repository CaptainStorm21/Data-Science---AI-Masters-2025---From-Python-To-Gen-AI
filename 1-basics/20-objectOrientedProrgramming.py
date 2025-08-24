####
# n. OOP is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphism, and encapsulation in programming. The main concept of OOP is to bind the data and functions that work on that data together as a single unit, so that no other part of the code can access the data.
# Major Concepts in OOP
# Some of the major concepts in OOP are:
# Classes and objects
# Polymorphism
# Encapsulation
# Inheritance
###

#Creating Classes and Objects
# When writing code in Python or Java, the first step is to define a class. Methods are defined within classes. For example, let us create a class with attributes length and breadth, and an __init__ function, which is the constructor of the class. The self parameter refers to the newly created instance of the class. The attributes length and breadth are associated with self to identify them as instance variables.
#

# the class name is Rectangle, and __init__ is the constructor. self refers to the newly created instance. length and breadth are instance variables, and the values 10 and 5 are assigned to them.
class Rectangle:
    def __init__(self):
        self.length = 10
        self.breadth = 5
# Instantiating Objects and Accessing Attributes
#To instantiate the class object
rect = Rectangle()

#You can access the attributes using the class object:
print(rect.length)
print(rect.breadth)

# Parameterized Constructor
# A parameterized constructor dynamically assigns attribute values during object creation. Instead of hardcoding values, you can pass them as arguments.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
#you can instantiate the class with different values:
rect = Rectangle(40, 20)

# Class Variables and Instance Variables
# length and breadth are instance variables. Class variables are defined within the class but outside any instance methods. For example:
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        
#pi is a class variable, while radius is an instance variable. When you instantiate the class, you can access both variables.

circle = Circle(5)
print(circle.radius)
print(circle.pi)
Circle.pi = 3.1436