# Using format to input the value of list
# This can be possible because of curly braces act as 'placeholder'
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

# Name the placeholders
a = "{x}, {y}".format(x=5, y=12)
print(a)

# Change the position of the placeholders
str = "{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)

# Use join as a separator
x = ", ".join(["spam", "eggs", "ham"])
print(x)

# Add String with separator on the list
str = "some text goes here"
x = str.split(' ')
print(x)

# Replace the substring with another String
x = "Hello ME"
print(x.replace("ME", "world"))

# Turn the string into Uppercase
print("This is a sentence.".upper())

# Turn the string into Lowercase
print("AN ALL CAPS SENTENCE".lower())

# Check the max value of strings
txt = "hello"
print(max(txt))
