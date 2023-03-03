def squares(n):
    num = 0
    while num <= n:
        yield num ** 2
        num += 1


n = int(input())
print(list(squares(n)))