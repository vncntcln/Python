# Re-assigned index of list
nums = [5, 8, 2]
nums[1] = 42

print(nums)

# Concatenation Lists
nums = [1, 2, 3]
print(nums + [4, 5, 6])

# Multiplied Lists
nums = [1, 2, 3]
print(nums * 3)

# Check lists item
# If item occurs one or more times in the lists then 'True' if not 'False'
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

# Excercises
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])
