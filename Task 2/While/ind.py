max = 0
ind = -1
a = -1
len = 0
while a!= 0:
    a = int(input())
    if a > max:
        max = a
        ind = len
    len += 1
print(ind)