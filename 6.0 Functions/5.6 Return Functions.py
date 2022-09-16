# Return Functions
def sum(x, y):
    return x+y

# Function to assign value


def sum(x, y):
    return x+y


res = sum(42, 7)
print(res)

# Returning Function


def foo(x, y):
    if x >= y:
        return x
    else:
        return y


x = foo(4, 7)
print(x)

# Returning Function


def max(x, y):
    if x >= y:
        return x
    else:
        return y


if (max(6, 4) > 10):
    print("Yes")
else:
    print("Nope")

# Returning Function


def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")


print(add_numbers(4, 5))

# Highest number that get returned is '2'


def print_numbers():
    print(1)
    print(2)
    return
    print(4)
    print(6)

# Return value using list


def double(a, b):
    return [a*2, b*2]


x = double(6, 9)
print(x)
