def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        for i in range(n - 2):
            new = listA + listB
            listA = listB
            listB = new
        return listB

print(nth_fib_lists([1], [2], 1))
