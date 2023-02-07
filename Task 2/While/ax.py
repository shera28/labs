p = -1
c = 0
m= 0
a = int(input())
while a!= 0:
    if p == a:
        c += 1
    else:
        p = a
        m= max(m, c)
        c = 1
    a= int(input())
m = max(m, c)
print(m)