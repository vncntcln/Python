# Boolean comparing the value
a = True
print(a)

print(2 == 3)

print("Hello" == "Hello")

# Comparison
x = 7

print(x != 8)
print(x > 5)
print(x < 2)
print(x >= 7)
print(x <= 7)

# Represent integers as '1' and '0'
x = (7 > 5)
print(int(x))

# Boolean logic 'and'
if (1 == 1) and (2 + 2 > 3):
    print("true")
else:
    print("false")

# Boolean logic 'or'
print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3 > 6)

# Boolean logic 'not'
print(not 1 == 1)

print(not 1 > 7)

# Practice
age = int(input())

if (age > 0 and age <= 11):
    print("Child")
elif (age >= 12 and age <= 17):
    print("Teen")
else:
    print("Adult")
