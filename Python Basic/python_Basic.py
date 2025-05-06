# 1-10: Variables and Data Types
x = 10
y = 5.5
name = "Shawon"
is_active = True
a, b, c = 1, 2, 3
PI = 3.1416
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"name": "Shawon", "age": 22}

# 11-20: Basic Input and Output
print("Hello, World!")
name = input("Enter your name: ")
print("Welcome,", name)
age = int(input("Enter your age: "))
print("In 5 years, you'll be", age + 5)
print("Name length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Starts with S?", name.startswith("S"))
print("Ends with n?", name.endswith("n"))

# 21-30: Conditional Statements
num = 7
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

