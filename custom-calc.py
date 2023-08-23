# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!


print("Please enter all 5 values to calculate the mean!")

v1 = input("Value 1:")
v2 = input("Value 2:")
v3 = input("Value 3:")
v4 = input("Value 4:")
v5 = input("Value 5:")

v1 = int(v1)
v2 = int(v2)
v3 = int(v3)
v4 = int(v4)
v5 = int(v5)

result = (v1 + v2 + v3 + v4 + v5)/5

print(f"The Mean of your sequence, {v1},{v2},{v3},{v4},{v5}, is \033[1m{result}\033[1m . Thank you!")