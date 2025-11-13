"""
Backjoon_2167 - 2차원 배열의 합 - S5

문제
- 2차원 배열이 주어졌을 때 (i,j) 위치부터 (x,y) 위치까지
- 저장되어 있는 수들의 합을 구하는 문제
"""

import sys
input = sys.stdin.readline

def calculate(i, j, x, y):
    result = 0
    for a in range(i, x+1):
        for b in range(j, y+1):
            result += arr[a][b]
    return result

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(calculate(i-1,j-1,x-1,y-1))