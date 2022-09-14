# Slices the amount of list
# The lists count the second paramters 'x - 1' only integers
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

# Slice at the end of the list 'before'
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])

# Count of the list parameters is real time when it comes to String
list = ["a", "b", "c", "d"]

a = list[0:2]
print(a)

# Slices start of 7 in the list 'after'
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])

# Lists captured by 2 step
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

# Lists start from 1 and take 4 step
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

# Take the first list parameters and -1 from lists
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

# Reverse list
nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res)

# Last list slices
a = input()

print(a[-1])
