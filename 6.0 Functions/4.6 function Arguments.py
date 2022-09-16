# Arguments can defined to generate function
def exclamation(word):
    print(word + "!")


exclamation("spam")

# Call the same functions with different arguments


def exclamation(word):
    print(word + "!")


exclamation("spam")
exclamation("eggs")
exclamation("python")

# Define functions with more than one arguments


def print_sum_twice(x, y):
    print(x + y)
    print(x + y)


print_sum_twice(5, 8)
