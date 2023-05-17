def nats(n):
    yield n
    yield from nats(n + 1)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n != 0 )

p = (sieve(nats(2)))

i = 0
while i < 5:
    print(next(p))
    i += 1

def foo(7):
    while n > 1:
        rem =









