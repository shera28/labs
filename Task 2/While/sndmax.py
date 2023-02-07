fst = int(input())
snd = int(input())
if fst < snd:
    fst, snd= snd, fst
a= int(input())
while a!= 0:
    if a > fst:
        snd, fst = fst, a
    elif a > snd:
        snd = a
    a = int(input())
print(snd)