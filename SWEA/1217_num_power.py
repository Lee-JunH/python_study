"""
SWEA_1217 - 거듭제곱 - D3

문제
- N, M이 주어질 때 N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출로 구현하라.
"""


def power(num, cnt):
    if cnt == M:
        return 1
    return num * power(num, cnt + 1)


T = 10
for _ in range(T):
    case = int(input())
    N, M = map(int, input().split())

    result = power(N, 0)
    print(f"#{case} {result}")
