def solution(n: int) -> int:
    total = 0
    weeks = 0

    while n:
        for i in range(1, 8):
            total += i + weeks
            n -= 1
            if n == 0:
                break
        weeks += 1
    return total


def solution2(n: int) -> int:
    total = 0
    weeks = n // 7
    rest = n % 7
    for i in range(0, weeks):
        total += (1 + i + 7 + i) * 7 / 2
    if rest != 0:
        for i in range(1, rest + 1):
            total += weeks + i
    return int(total)
