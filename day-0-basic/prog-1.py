from sys import argv
sum = 0
v = argv[1:]
for x in v:
    n = int(x)
    sum = sum +n
print('Sum is', sum)