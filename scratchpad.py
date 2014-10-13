def genPrimes():
    yield 1
    yield 2


def prime(n):
    a = n
    for i in range(a,n):
        if n%i == 0:
            return False
        a-=1
    if i == n:
        return True

print prime(3)



