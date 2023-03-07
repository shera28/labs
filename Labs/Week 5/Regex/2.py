import re

text = input()

print(re.findall('ab{2,3}', text))