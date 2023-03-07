import re
text = input()
a= re.findall('[A-Z]', text)
b = ['_' + i.lower() for i in a]
cnt = 0
for i in a:
    r = re.search('[A-Z]+', text)
    if r:
        n = text.find(i)
        text = text[:n] + b[cnt] + text[n + 1:]
    cnt += 1
print(text)