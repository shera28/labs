import re

text = input()

print(re.findall('ab*', text))