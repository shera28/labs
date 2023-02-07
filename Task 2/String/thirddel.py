s = input()
a = ''
for i in range(len(s)):
    if i % 3 != 0:
        a = a + s[i]
print(a)