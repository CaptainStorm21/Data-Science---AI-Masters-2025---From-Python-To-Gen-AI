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
import math


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

# Now, the value of pi has changed for all instances of the class.

# Adding Methods to a Class
# You can add methods to a class, such as a method to calculate the area of a rectangle.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        return self.length * self.breadth

# You can instantiate the class and call the method:
# This will output 50, as the area is 10 multiplied by 5.
rect = Rectangle(10, 5)
print(rect.calculate_area())

# The Significance of self
# The attributes length and breadth are associated with an instance. self ensures that each instance refers to its own copy of attributes.

# Inheritance and Overriding
# Inheritance allows a child class to access properties and methods of a parent class. For example:
class Employee:
    def function1(self):
        print('hello world')

class Department(Employee):
    pass

#You can instantiate the child class and call the parent class method:

dept = Department()
dept.function1()

# This will print 'hello world' because the child class inherits the method from the parent class.









## Method Overriding and Abstract Methods
# A parent class can define a method without logic (abstract), and child classes can override it with their own logic.

class Shape:
    def set_color(self, color):
        self.color = color
    def calculate_area(self):
        pass
class Circle(Shape):
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return Circle.pi * self.radius
c = Circle(5)
c.set_color('red')
print(c.calculate_area())

# Similarly, you can define a Rectangle class inheriting from Shape and override the calculate_area method.
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        return self.length * self.breadth

#the calculate_area method is overridden in each child class, demonstrating the concept of method overriding.
r = Rectangle(5, 10)
r.set_color('blue')
print(r.calculate_area())


# Key Takeaways
# Object-Oriented Programming (OOP) in Python uses classes and objects to model real-world entities.
# Constructors, class variables, and instance variables are fundamental concepts in OOP.
# Inheritance allows child classes to access properties and methods of parent classes, and method overriding enables customization in child classes.
# The self keyword ensures each instance maintains its own attributes.

##In Python, if you create another class, you cannot directly refer to self.length from the Rectangle class unless you create an instance of the Rectangle class within the new class.
# Here's how it works conceptually:
# Class Definition: When you define the Rectangle class with its __init__ method, you define the properties self.length and self.breadth.
# Creating Instances: For any new class to access these properties, you'd typically create an instance of the Rectangle class. For example:
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class AnotherClass:
    def __init__(self):
        self.rect = Rectangle(10, 5)  # Create an instance of Rectangle

    def show_dimensions(self):
        return self.rect.length, self.rect.breadth

obj = AnotherClass()
print(obj.show_dimensions())  
# This will print (10, 5)

#Instance Access: In the AnotherClass, self.rect.length and self.rect.breadth refer to the attributes of the Rectangle instance created. Thus, you rely on self.length by creating an instance of Rectangle.


radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area}")


### Notes:
# The __init__ method is often referred to as a constructor. It is called automatically when you create an object of the class, and it sets up the initial state of the object. In the context of your answer, you could refine it to say: "The __init__ method is used to initialize the instance variables of the class when creating an object."It does not instantiate the class method itself but rather prepares the instance with any necessary values.

# Instance Variable: This is a variable that is specific to an instance of a class. It is defined within the __init__ method (or any method) using self, and each object can have different values for these variables.
# Class Variable: This is shared across all instances of a class. It is defined within the class body but outside any methods. Because of this, all instances of the class can share and access this variable.


# # Polymorphism in object-oriented programming is the concept that allows methods to do different things based on the object it is acting upon. This means you can use a single interface (method) to represent different underlying forms (objects). Polymorphism often occurs through method overriding in subclasses or through implementing the same method in different classes.
# For example, consider a parent class Shape with a method calculate_area. You can have subclasses like Circle and Rectangle that implement this method in their own way, using the formula relevant to their specific shapes:
    
    
class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width