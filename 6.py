n = int(input())

if n == 0:
    print([])
else:
    divisors = set()

    i = 1
    while i * i <= abs(n):
        if abs(n) % i == 0:
            divisors.add(i)
            divisors.add(abs(n) // i)
        i += 1

    print(sorted(divisors))