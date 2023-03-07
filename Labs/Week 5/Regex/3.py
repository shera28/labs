import re

text = input()

print(re.findall('[a-z]+,[a-z]+', text))