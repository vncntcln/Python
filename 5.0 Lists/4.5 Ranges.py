# Convert lists of range
numbers = list(range(10))
print(numbers)

# Call specific item lists in range
nums = list(range(5))
print(nums[4])

# Produces value from the 'first' to 'second' parameters
# Remember, the second argument is not included in the range, so range(3, 8) won’t include the number 8.
numbers = list(range(3, 8))
print(numbers)

# Check the size of the lists range
print(range(20) == range(0, 20))

# Print lists range with interval
# Third parameters '2' is counted as interval
numbers = list(range(5, 20, 2))
print(numbers)

# Print lists range with interval backward
x = list(range(7, 3, -1))
print(x)

# Ranges with for loops
for i in range(5):
    print("hello!")

# Input the number range of lists
x = list(range(0, 99))
print(x[4])
