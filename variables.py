# What does every Python variable have? 1. A name; 2. A value (the content of the container)
var = 1
print(var)

# You can use the print() statement and combine text and variables
# using the + operator to output strings and variables, e.g.:
var = "3.7.1"
print("Python version: " + var)

# Assigning a new value to an already existing variable
var = 1
print(var)
var = var + 1
print(var)

# Do you know what the output of the following snippet will be?
var = 100
var = 200 + 300
print(var)
# 500 - why? Well, first, the var variable is created and assigned
# a value of 100. Then, the same variable is assigned a new value:
# the result of adding 200 to 300, which is 500.

# Pythagorean theorem:
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

# LAB
john = 3
mary = 4
adam = 6
print("John: " + "3", "Mary: " + "4", "Adam: " + "6", sep=", ", end=".")
print()
totalApples = john + mary + adam
print(totalApples)

# Shortcut operators
# x = x * 2               # or x *= 2       They have the same effect
# sheep = sheep + 1       # or sheep += 1
# i = i + 2 * j ⇒ i += 2 * j
# var = var / 2 ⇒ var /= 2
# rem = rem % 10 ⇒ rem %= 10
# j = j - (i + var + rem) ⇒ j -= (i + var + rem)
# x = x ** 2 ⇒ x **= 2

# LAB
kilometers = 12.25
miles = 7.38

miles_to_kilometers = 7.38 * 1.61
kilometers_to_miles = 12.25 / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# 1 real is equal to 5.2 euros
euros = 15
reais = 20

real_to_euro = 20 / 5.2
euro_to_real = 15 * 5.2

print(reais, "reais are", round(real_to_euro, 2), "euros")
print(euros, "euros are", round(euro_to_real, 2), "reais")

# LAB
x = 0   # x = 1 and x = -1
x = float(x)
y = ((3*x**3)-(2*x**2)+(3*x)-1)
print("y =", y)

# Summary exercises
# Exercise 1
# What is the output of the following snippet?
var = 2
var = 3
print(var)

# Check: 3

# Exercise 3
# What is the output of the following snippet?
a = '1'
b = "1"
print(a + b)

# Check 11

# Exercise 4
# What is the output of the following snippet?
a = 6
b = 3
a /= 2 * b
print(a)

# Check: 1.0
# Why? --> 2 * b = 6
#          a = 6 → 6 / 6 = 1.0
