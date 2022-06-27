def recursion(start, primesL, limit):
    if start > limit:
        return []
    variants = [start]
    for p in primesL:
        variants += recursion(start * p, primesL, limit)
    variants = list(set(variants))
    return variants


def count_find_num(primesL, limit):
    start = 1
    for digit in primesL:
        start *= digit
    result = recursion(start, primesL, limit)
    if result:
        return [len(result), max(result)]
    return []


if __name__ == '__main__':
    count_find_num()
