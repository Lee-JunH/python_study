"""
Backjoon_11660 - 구간 합 구하기5 - S1

문제
- N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 문제
"""

import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

my_map = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        my_map[i][j] = my_map[i][j-1] + my_map[i-1][j] - my_map[i-1][j-1] + maps[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    prefix_sum = my_map[x2][y2] - my_map[x2][y1-1] - my_map[x1-1][y2] + my_map[x1-1][y1-1]
    print(prefix_sum)