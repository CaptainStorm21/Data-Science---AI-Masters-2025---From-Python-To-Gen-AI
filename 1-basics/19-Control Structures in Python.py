# odd and even
x = 51
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
x = 10
if x % 2 == 0:
    print(str(x) + " is an even number")
else:
    print(str(x) + " is an odd number")
    
age = 61
if age < 18 or age > 60:
    print("Going to the party")
else:
    print("Not going")
    
x = int(input("Enter your age: "))
if x <= 18 or x >= 60:
    print("Welcome to the party")
else:
    print("Sorry, you do not fit in the PM's age criteria")
    
    total = 6000
if total > 5000:
    discount = 1000
elif total > 2500:
    discount = 500
else:
    discount = 100
print("Discount applied:", discount)

# interate over the range of values
for i in range(1, 5):
    print(i, end='.')
    
