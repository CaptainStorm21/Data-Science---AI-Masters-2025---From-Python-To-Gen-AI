name = input ("Enter your name: ")
age = int(input("Enter your age: "))
print ("Hello " + name + ", you are " + str(age) + " years old.")

acc = 1000.50
# float 
float(acc)
print(acc)
type(acc)

# float to int conversion
account = int(acc) 
print(account)
type(account)

# from num to string conversion
num = 12345
num_str = str(num)
print(num_str)
print("The type is", type(num_str))

# from string to float 
str_num = "12345.67"
str_num_float = float(str_num)
print(str_num_float)
print("The type is", type(str_num_float)) 

# from string to int
str_num_int = int(float(str_num))
print(str_num_int)
print("The type is", type(str_num_int)) 

# frpmt string to array
my_string = "hello"
char_list = list(my_string)
print(char_list)

# find index of a character in an array
my_list = [10, 20, 30, 40, 50]
element_to_find = 30
index = my_list.index(element_to_find)
print(f"The index of {element_to_find} is: {index}")

# addition, substraction, multiplication, division

a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
# Modulus operation
print("Modulus:", a % b)        
# Exponentiation
print("Exponentiation:", a ** b)
# Floor division
print("Floor Division:", a // b)
# Comparison operators
print("Is a equal to b?", a == b)

# Logical operators
print("Is a greater than b?", a > b)
print("Is a less than b?", a < b)
print("Is a not equal to b?", a != b)

# Bitwise operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT of a:", ~a)
print("Bitwise NOT of b:", ~b)
# Identity operators
print("Is a identical to b?", a is b)
print("Is a not identical to b?", a is not b)       

# Membership operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)
print("Is 6 not in my_list?", 6 not in my_list)

# Assignment operators
x = 10
print("Initial value of x:", x)
x += 5  
print("After x += 5, x is:", x)
x -= 3  
print("After x -= 3, x is:", x)         
x *= 2
print("After x *= 2, x is:", x)
x /= 4      
print("After x /= 4, x is:", x)
x %= 3
print("After x %= 3, x is:", x)
x **= 2
print("After x **= 2, x is:", x)
x //= 2
# floor division
print("After x //= 2, x is:", x)        

# Ternary operator
a = 5
b = 10
max_value = a if a > b else b
print("The maximum value is:", max_value)       

# Type casting examples
# Implicit type casting
x = 10    # int
y = 3.14  # float
result = x + y  # x is implicitly converted to float
print("Result of implicit type casting:", result)
# Explicit type casting
x = 10.5  # float
y = int(x)  # x is explicitly converted to int
print("Result of explicit type casting:", y)            

# Reassigning letters
word_string = "England"
word_list = list(word_string)
print("Original word:", word_list)
new_letter = word_string.replace('E', 'A')
print("Modified word:", new_letter)