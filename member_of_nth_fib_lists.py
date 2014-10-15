from nth_fib_lists import nth_fib_lists as fibo


def member_of_nth_fib_lists(listA, listB, needle):
    l = 0
    c = 1
    while l <= len(needle):
        l = len(fibo(listA, listB, c))
        if fibo(listA, listB, c) == needle:
            return True
        c = c + 1
    return False


print(member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
