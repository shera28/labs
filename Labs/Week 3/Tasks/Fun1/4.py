def filter_prime(list):
    prime = True
    primes = []
    for i in list:
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
           primes.append(i)
        prime = True
    return primes



print(filter_prime(range(2, 101)))