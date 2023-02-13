def palindrome(s):
    arr = list(s)
    arr.reverse()
    ss = ''.join(arr)
    if s == ss:
        return True
    else:
        return False

print(palindrome(input()))