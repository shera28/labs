import re

text = input()

print(re.findall('^a.+b$', text))