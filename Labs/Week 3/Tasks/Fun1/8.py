def has_007(string):
    if "007" in string:
        return True
    else:
        return False


s = ''
arr = [1,2,4,0,0,7,5]
for i in arr:
    s += str(i)
print(has_007(s))