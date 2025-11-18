"""
SWEA_5188 - 최소합 - D3

문제
- NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
- 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되는 합계
"""

from collections import deque

def bfs():
    global min_hap

    my_q = deque()
    my_q.append((0,0,board[0][0]))
    dr = [0, 1]
    dc = [1, 0]

    while my_q:
        r, c, hap = my_q.popleft()
        if r == N-1 and c == N-1:
            min_hap = min(min_hap, hap)
            continue

        for dir in range(2):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if hap+board[nr][nc] > min_hap:
                continue
            my_q.append((nr, nc, hap+board[nr][nc]))


T = int(input())
for case in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    min_hap = 261

    bfs()
    print(f'#{case+1} {min_hap}')



# 3
# 3
# 1 2 3
# 2 3 4
# 3 4 5
# 4
# 2 4 1 3
# 1 1 7 1
# 9 1 7 10
# 5 7 2 4
# 5
# 6 7 1 10 2
# 10 2 7 5 9
# 9 3 2 9 6
# 1 6 8 2 9
# 8 3 8 2 1