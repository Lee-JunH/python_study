"""
SWEA_5188 - 최소합 - D3

문제
- NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
- 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되는 합계
"""

def dfs(x, y, hap):
    global min_hap

    if x >= N or y >= N:
        return
    if hap > min_hap:
        return
    if x == N-1 and y == N-1:
        min_hap = min(min_hap, hap)
        return
    
    if x + 1 < N:
        dfs(x+1, y, hap+board[x+1][y])
    if y + 1 < N:
        dfs(x, y+1, hap+board[x][y+1])

T = int(input())
for case in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    min_hap = 261
    dfs(0,0,board[0][0])
    print(f'#{case+1} {min_hap}')

# from collections import deque

# def bfs():
#     global min_hap

#     my_q = deque()
#     my_q.append((0,0,board[0][0]))
#     dr = [0, 1]
#     dc = [1, 0]

#     while my_q:
#         r, c, hap = my_q.popleft()
#         if hap > min_hap:
#             continue
#         if r == N-1 and c == N-1:
#             min_hap = min(min_hap, hap)
#             continue

#         for dir in range(2):
#             nr = r + dr[dir]
#             nc = c + dc[dir]
#             if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                 continue
#             my_q.append((nr, nc, hap+board[nr][nc]))


# T = int(input())
# for case in range(T):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]

#     min_hap = 261

#     bfs()
#     print(f'#{case+1} {min_hap}')