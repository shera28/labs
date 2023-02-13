def histogram(l):
    for i in l:
        for j in range(i):
            print('*', end=(""))
        print()


arr = [4, 9, 7]
histogram(arr)