class Filt:
    def __init__(self, arr):
        self.arr = arr

    def f(self):
        self.farr = filter(lambda x : ff(x), self.arr)
        return list(self.farr)

def ff(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a = Filt([1, 2, 4, 6, 8, 964, 3, 45, 7576, 86567])
print(a.f())