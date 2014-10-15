def simplify_fraction(fraction):
    numerator = int(fraction[0])
    denominator = int(fraction[1])
    for n in range(min(numerator, denominator), 1, -1):
        if numerator % n == 0 and denominator % n == 0:
            numerator = numerator // n
            denominator = denominator // n
    return(numerator, denominator)

print(simplify_fraction("3", "9"))
