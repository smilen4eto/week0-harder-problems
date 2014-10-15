def sort_fractions(fractions):
    new = []
    result = []
    for n in fractions:
        fr = n[0] / n[1]
        new.append([fr, n])
    new.sort()
    for i in new:
        result.append(i[1])
    return result

print(sort_fractions([(2, 3), (1, 2)]))
