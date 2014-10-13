def genPrimes():
    n = 2
    primes = []
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 1

test = genPrimes()

print test.next()
print test.next()
print test.next()
print test.next()
print test.next()
print test.next()
print test.next()




