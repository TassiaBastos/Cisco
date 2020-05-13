# Exponentiation
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# Multiplication
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

# Division
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
# The result produced by the division operator is always a float,
# regardless of whether or not the result seems to be a float at
# first glance: 1 / 2, or if it looks like a pure integer: 2 / 1.

# Integer division
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)   # The result of integer division is always rounded
# to the nearest integer value that is less than
# the real (not rounded) result.
# This is very important: rounding always goes to the lesser integer!!!
print(6. // 4)  # returns a float number

print(-6 // 4)
print(6. // -4)
# The result is two negative twos. The real (not rounded) result is
# -1.5 in both cases. However, the results are the subjects of rounding.
# The rounding goes toward the lesser integer value, and the lesser
# integer value is -2, hence: -2 and -2.0.

# Remainder (modulo)
print(14 % 4)
print(12 % 4.5)

# Addition
print(-4 + 4)
print(-4. + 8)

# Subtraction
print(-4 - 4)
print(4. - 8)
print(-1.1)

# Operators and their priorities
var = 2 + 3 * 5     # left-sided bindings
print(var)

# Operators and their bindings
print(9 % 6 % 2)    # left-sided bindings

# Operators and their bindings: exponentiation
print(2 ** 2 ** 3)
# The result clearly shows that the exponentiation operator uses right-sided binding.

# List of priority
print(2 * 3 % 5)

# Operator and parentheses
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# Exercise 1
# What is the output of the following snippet?
print((2 ** 4), (2 * 4.), (2 * 4))
# Exercise 2
# What is the output of the following snippet?
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# Exercise 3
# What is the output of the following snippet?
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
