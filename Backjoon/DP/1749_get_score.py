"""
Backjoon_1749 - 점수 따먹기 - G4

문제
- NxM행렬에서 각 칸에 -10,000 이상 10,000 이하의 정수를 하나씩 쓴다.
- 그 행렬의 부분행렬을 그려 그 안에 적힌 정수의 합을 구하는 게임이다.
- 정수의 합이 최대가 되는 부분행렬을 구하는 문제

풀이
- 최대 합을 구하기 위해 이전까지의 합을 이용해야하는 문제
- DP를 이용하는 문제이다.
- 각 위치에서의 최대 합을 구하고 그 값을 이용하여 부분행렬을 구간을 설정하여 최대 합을 구할 수 있다.
    - 이 방법은 다중 for문 방식이기 때문에 시간이 너무 오래 걸린다.

- N, M은 최대 200
- 최대 시간은 200^4 = 1,600,000,000 16억
- 파이썬에서 3천만번의 연산이 1초에 가능하다.
- 즉 이 코드는 50초 정도의 시간이 예상된다.

- 200^3 = 8,000,000 8백만번
- 1초 안에 연산이 가능하다.
- 3중 for문일 때 시간초과가 안날것 같다.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

max_mat = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        max_mat[i][j] = max_mat[i-1][j] + max_mat[i][j-1] - max_mat[i-1][j-1] + matrix[i - 1][j - 1]

max_hap = -float('inf')

for x1 in range(1, N+1):
    for y1 in range(1, M+1):
        for x2 in range(x1, N+1):
            for y2 in range(y1, M+1):
                total = max_mat[x2][y2] - max_mat[x1 - 1][y2] - max_mat[x2][y1 - 1] + max_mat[x1 - 1][y1 - 1]
                max_hap = max(max_hap, total)

print(max_hap)


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

max_mat = [[0 for _ in range(M+1)] for _ in range(N+1)]