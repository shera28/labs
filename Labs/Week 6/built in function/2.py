s = input()
l = 0
u = 0
for x in s:
    if x.islower():
        l += 1
    if x.isupper():
        u += 1

print(f"lower: {l}\nupper: {u}")