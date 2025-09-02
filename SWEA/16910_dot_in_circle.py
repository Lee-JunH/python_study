"""
SWEA_16910 - 원안의 점 - D3

문제
- N이 주어질 때, 원점을 중심으로 반지름이 N인 원 안에 포함되는 격자점의 개수를 구하라

풀이
- x^2 + y ^2 <= N^2 인 좌표 개수를 구한다.
"""

T = int(input())
for case in range(T):
    N = int(input())

    cnt = 0
    for i in range(-N, (N+1)):
        for j in range(-N, (N+1)):
            if i**2 + j**2 <= N**2:
                cnt += 1
    print(f'#{case+1} {cnt}')