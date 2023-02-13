def unique(list):
    cnt = 0
    arr = []
    for i in list:
        for j in list:
            if i == j:
                cnt += 1
        if cnt == 1:
           arr.append(i)
        cnt = 0
    return arr

print(unique([1, 2, 3, 1, 4]))