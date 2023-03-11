import time
import math

n = int(input())
s = int(input())

time.sleep(s / 1000)
print(f"Square root of {n} after {s} miliseconds is {math.sqrt(n)}")