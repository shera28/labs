import re

text = input()

text2 = re.sub('( |,|\.)', '-', text)
print(text2)