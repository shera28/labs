def div(n):
    num = 0
    while num <= n:
        if num % 3 == 0 and num % 4 == 0:
            yield num
        num += 1


n = int(input())
print(list(div(n)))