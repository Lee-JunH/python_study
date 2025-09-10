"""
backjoon_11501 - 주식 - S2

문제
- 미래를 예측하여 주가를 예상할 수 있다.
- 날 수가 주어지고 주가가 주어질 때 최대 이익을 구하는 문제이다.

풀이
- 가장 큰 값을 찾아서 그 앞의 값들과의 차를 더한다.
- 이후 인덱스 부터 큰 값을 찾아 계속 진행한다.
"""

import sys
input = sys.stdin.readline

T = int(input())
for case in range(T):
    N = int(input())
    jusik = list(map(int, input().split()))

    i = 0
    profit = 0
    max_j = max(jusik[i:])
    for i in range(N):
        if jusik[i] == max_j:
            if i == N-1:
                break
            max_j = max(jusik[i+1:])
            continue
        profit += max_j - jusik[i]
    print(profit)