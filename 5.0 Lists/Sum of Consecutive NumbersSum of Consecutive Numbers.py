N = int(input())
# your code goes here
a = N
x = range(1, N + 1)
for i in x:
    N = i + N
print(N-a)
