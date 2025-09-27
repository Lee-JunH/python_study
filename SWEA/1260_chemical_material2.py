"""
SWEA_1260 - 화학물질2 - D6

문제
- 창고에는 화학 물질 용기 n^2개가 nxn 으로 배열되어 있었다.
- 빈 용기에 해당하는 원소는 '0'으로 저장하고 화학물질은 1~9 사이의 정수를 저장한다.
- 특징
    - 화학 물질이 담긴 용기들은 사각형이고 빈 용기는 없다.
    - 다른 화학물질과는 한칸이상 떨어져있다.
"""

from collections import deque

def check(r, c):
    my_r = 0
    for a in range(r, n):
        if chemical[a][c] == 0:
            break
        my_c = 0
        for b in range(c, n):
            if chemical[a][b] == 0:
                break
            my_c += 1
            visited[a][b] = 1
        my_r += 1
    return (my_r, my_c)

# a~b까지의 최소 합 구하기
def count_gop(a, b):
    if a == b:  # 같을 때는 0
        return 0
    
    if dp[a][b] != 0:
        return dp[a][b]
    
    temp = float('inf')
    for i in range(a, b):
        num = s_matrix[a][0] * s_matrix[i][1] * s_matrix[b][1]
        temp = min(temp, count_gop(a, i) + count_gop(i+1, b) + num)
    dp[a][b] = temp

    return dp[a][b]

T = int(input())
for case in range(T):
    n = int(input())
    chemical = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0 for _ in range(n)] for _ in range(n)]
    matrix = []

    # 행렬 찾기
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and chemical[i][j] != 0:
                matrix.append(check(i, j))

    # 행렬 곱의 최소 횟수 구하기
    my_dict = {}
    keys = set()
    values = set()
    for m, n in matrix:
        my_dict[m] = n
        keys.add(m)
        values.add(n)
    for k in keys:
        if k not in values:
            first = k
            break

    s_matrix = []
    while len(s_matrix) != len(matrix):
        s_matrix.append((first, my_dict[first]))
        first = my_dict[first]

    dp = [[0] * len(s_matrix) for _ in range(len(s_matrix))]
    result = count_gop(0, len(s_matrix)-1)

    print(f"#{case+1} {result}")