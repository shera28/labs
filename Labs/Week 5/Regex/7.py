import re
text = input()
cnt = 0
arr = re.findall('_.', text)
letters = []
for i in arr:
    letters.append(i[1].upper())
for i in arr:
    a = text.find(str(i))
    text = text[:a] + letters[cnt] + text[a + 2:]
    cnt += 1
print(text)