def is_prime(n):
    p = n
    if n == 2:
        return True
    else:
        for i in (2, n):
            if p % i == 0:
                return False
            else:
                return True