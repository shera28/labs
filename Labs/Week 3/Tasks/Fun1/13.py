import random

print('Hello! What is your name?')
n = input()

print(f"Well, {n}, I am thinking of a number between 1 and 20.")
print('Take a guess.')
g = int(input())
r = random.randint(0, 20)
c = 0

while True:
    if r == g:
        print(f"Good job, {n}! You guessed my number in {c} guesses!")
        break
    else:
        if g > r:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
    print("Take a guess")
    g = int(input())
    c += 1