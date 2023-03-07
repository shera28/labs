import re

text = input()

print(re.findall('[A-Z][a-z]+', text))