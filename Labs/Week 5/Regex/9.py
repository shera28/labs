import re
text = input()
a = text.split()
for i in range(len(a) - 1):
    res1 = re.match('[A-Z]', a[i])
    res2 = re.match('[A-Z]', a[i + 1])
    if res1 and res2:
        a.insert(i + 1, "    ")
s = ' '.join(a)
print(s)