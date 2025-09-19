"""
SWEA_22654 - 차윤이의 RC카 - D2

문제
- NxN 필드가 주어진다.
    - 'G' : RC카가 이동 가능한 땅
    - 'T' : RC카가 이동이 불가능한 나무
    - 'X' : 현재 RC카의 위치
    - 'Y' : RC카를 이동 시키고자 하는 위치
- 조종기가 주어진다.
    - 'A' : 앞으로 이동
    - 'L' : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
    - 'R' : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전
- 처음 시작 방향은 위

- 목적지에 도달 할 수 있는지 확인하는 문제

풀이
- dfs에 방향까지 추가해서 구현하자
"""

def find_start():
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                return (i,j)

def dfs(dir):
    for dir in range(3):
        nr = a
        nc = b
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if field[nr][nc] == 'T':
            continue
        if field[nr][nc] == 'Y':
            pass


T = int(input())
for case in range(T):
    N = int(input())
    field = [list(input().split()) for _ in range(N)]

    start_r, start_c = find_start()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dfs(start_r, start_c)