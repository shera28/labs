import os

path = "first.txt"
cnt = 0
a = open('first.txt', 'r')
for lines in a:
    cnt += 1
print(cnt)