from itertools import combinations


def bananas(s: str) -> set:
    result = set()
    for position_options in combinations(range(len(s)), len(s) - 6):
        list_from_s = list(s)
        for i in position_options:
            list_from_s[i] = '-'
        word = ''.join(list_from_s)
        if word.replace('-', '') == 'banana':
            result.add(word)
    return result


if __name__ == '__main__':
    bananas()
