a = int(input())
sum = 0
for i in range(1, a + 1):
    sum +=i
for i in range(a - 1):
    sum -= int(input())
print(sum)