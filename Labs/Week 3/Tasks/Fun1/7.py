def has_33(string):
    if "33" in string:
        return True
    else:
        return False


s = ''
arr = [2, 3, 3, 3]
for i in arr:
    s += str(i)
print(has_33(s))