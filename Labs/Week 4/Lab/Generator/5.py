def dec(a):
    while a >= 0:
        yield a
        a -= 1


a = int(input())

for b in dec(a):
    print(b)