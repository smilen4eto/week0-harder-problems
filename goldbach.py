from is_prime import is_prime as prime


def goldbach(n):
    new = []
    for i in range(2, n // 2 + 1):
        if prime(i) and prime(n - i):
            new.append((i, n - i))
    return new

print(goldbach(4))
