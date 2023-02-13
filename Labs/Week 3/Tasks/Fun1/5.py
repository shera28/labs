def Perm(string, start, end):
    if start == end - 1:
        print(string)
    else:
        for current in range(start, end):
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

            Perm("".join(x), start + 1, end)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp


str = input()
n = len(str)
Perm(str, 0, n)