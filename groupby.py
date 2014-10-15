from itertools import groupby as groupby_


def groupby(func, seq):
    sorted_list = sorted(seq, key=func)
    return {key: list(group) for key, group in groupby_(sorted_list, func)}

print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
