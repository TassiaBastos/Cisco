# imput() function
# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")

# The input() function with an argument
# the result of the input() function is a string!!!!!!!!!!
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# Type casting - to solve the function prohibited
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# or
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# Concatenation
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# Replication
# rectangle
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Type conversion: str()
# A function capable of doing that is called str():
# str(number)
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# LAB
variable_a = float(input("Input a value for variable a: "))
variable_b = float(input("Input a value for variable b: "))

print("The result of addition is: ", (variable_a + variable_b))
print("The result of subtraction is: ", (variable_a - variable_b))
print("The result of multiplication is: ", (variable_a * variable_b))
print("The result of division is: ", (variable_a / variable_b))
print("\nThat's all, folks!")

# LAB
x = float(input("Enter value for x: "))
y = (1/(x+(1/(x+(1/(x+(1/x)))))))
print("y =", y)

# LAB
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

end_hour = hour + (dura // 60)
end_mins = mins + (dura % 60)
end_hour += end_mins // 60
end_mins = end_mins % 60
end_hour = end_hour % 24

print(end_hour, ":", end_mins)
