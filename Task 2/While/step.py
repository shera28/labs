n=int(input())
t=2
p=1
while t <= n:
    t *= 2
    p += 1
print(p - 1, t // 2)