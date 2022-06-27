from math import log


def zeros(n: int) -> int:
    """Подсчет конечных нулей в факториле числа"""
    if n:
        k = log(n, 5)
        answer = 0
        for i in range(1, int(k) + 1):
            answer += n//(5**i)
        return answer
    else:
        return 0


if __name__ == '__main__':
    zeros()
