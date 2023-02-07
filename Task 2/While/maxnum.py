max = 0
n = 0
a = -1
while a!= 0:
    a = int(input())
    if a > max:
        max, n = a, 
    elif a == max:
        n += 1        
print(n)