def reverse(str):
    arr = list(str)
    arr.reverse()
    return ''.join(arr)


print(reverse(input()))