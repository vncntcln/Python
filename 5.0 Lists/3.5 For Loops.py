# For loops
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

# Multiplication list in the iteration
nums = [4, 7, 3, 1]
for x in nums:
    print(x*2)

# Count the letter 't' in the for-loops
str = "testing for loops"
count = 0

for x in str:
    if (x == 't'):
        count += 1

print(count)

# Usage of break in the for-loops iteration
text = "some text"
for x in text:
    if x == 'e':
        break
    print(x)

# Check each of the item in the lists and print it out
list = [2, 3, 4, 5, 6, 7]

for x in list:
    if (x % 2 == 1 and x > 4):
        print(x)
        break

# Practice I
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
b = 0

for a in x:
    b += a

print(b)

# Practice II
nums = [1, 2, 3, 4]
res = 0

for x in nums:
    if (x % 2 == 0):
        continue
    else:
        res += x

print(res)
4
