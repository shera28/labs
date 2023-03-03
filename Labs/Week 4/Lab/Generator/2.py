def evens(n):
    num = 1
    while num <= n:
        if num % 2 == 0:
            yield num
        num += 1


n = int(input())
print(list(evens(n)))