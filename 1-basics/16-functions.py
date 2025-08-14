# Functions 
def function_name (argument1, argument2):
    sum_objects = argument1 + argument2
    print(sum_objects)

function_name(3,3)

def fnct_odd_even (num):
    if num % 2 == 0:
        print(num, "is even")
    else: 
        print(num, "is odd")
fnct_odd_even(5)

# lambda function
#   small anon function to make develoers life easier 
#   can take any number of argument but have only one 
#   expression

# factorial
def factorial_func(n):
    fact = 1
    for i in range (1, n+1):
        fact = fact*i
        print ( fact, "is in power of", n)
factorial_func(5)

# sum of all natural numbers till the number provided
def sum_natural (n):
    num = 0 
    for i in range(1, n+1):
        num = num+i
    return num
print(sum_natural(5))


def func_1 (name, age = 30):
    print ("name ", name)
    print ("age ", age)
func_1("Dave", 23)


# Lambda functions
# lambda argument: expressions
x = lambda a: a+10
print (x(521))

x = lambda a: a%2==0
print (x(323))

z = lambda a: "even" if a % 2 == 0 else "odd"
print(z(221))

# add create lanbda fuction that adds 2 numbers

sum_int = lambda a,b: a+b
print (sum_int(3,2))

