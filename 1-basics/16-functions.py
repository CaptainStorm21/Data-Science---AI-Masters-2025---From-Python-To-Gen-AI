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


