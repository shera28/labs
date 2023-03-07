import re
text = input()
arr = re.split('[A-Z]', text)
print(arr)