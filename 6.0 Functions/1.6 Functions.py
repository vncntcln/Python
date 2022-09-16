# Take number item in a list 'len'
nums = [1, 3, 5, 2, 4]
print(len(nums))

# Return length of the String 'character count'
str = "some text"
x = len(str)
print(x)

# Add item to end of the list 'Append'
nums = [1, 2, 3]
nums.append(4)
print(nums)

# Add new item based on the position 'Insert'
words = ["Python", "fun"]
words.insert(0, "is")
print(words)

# Check the position of list item 'Index'
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))

# Check the position of item list
x = [2, 4, 5, 7, 4]
y = x.index(4)
print(y)

# Minimum 'min' and Maximum 'max' value at item list
x = [1, 8, 42, 3]

print(min(x))
print(max(x))

# Count how many item occurs in a list 'Count'
x = [2, 4, 6, 2, 7, 2, 9]
print(x.count(2))

# Remove item from a list
x.remove(4)
print(x)

# Reverse item on the list
x.reverse()
print(x)
