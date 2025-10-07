"""
Backjoon_7569 - 토마토 - G5

문제
- NxMxH의 크기의 상자에 토마토를 보관한다.
- 보관 후, 하루가 지나면 익은 토마토들의 인접한 곳의 토마토들이 익게 된다.
- 대각선 방향은 영향을 주지 못한다.
- 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 최소 일수를 구하는 문제

풀이
- 일반적인 bfs를 3차원으로 구현하였다.
- 문제는 한번 퍼졌을 때 하루가 지나야 한다.
- 처음 큐에 넣은 개수 만큼 뺐을 때 하루가 지나도록 만들자.
"""

from collections import deque

def bfs():
    day = 0
    cnt = 0
    count = len(q)
    while q:
        if cnt == count:
            cnt = 0
            count = len(q)
            day += 1
        cur = q.popleft()
        cnt += 1
        for dir in range(6):
            nr = cur[1] + dr[dir]
            nc = cur[2] + dc[dir]
            nh = cur[0] + dh[dir]
            if nr < 0 or nc < 0 or nh < 0 or nr >= N or nc >= M or nh >= H:
                continue
            if vis[nh][nr][nc] == 1 or tomato[nh][nr][nc] == -1 or tomato[nh][nr][nc] == 1:
                continue
            tomato[nh][nr][nc] = 1
            vis[nh][nr][nc] = 1
            q.append((nh, nr, nc))
    return day

def check_tomato():
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomato[h][r][c] == 0:
                    return 1
    return 0

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

q = deque()
vis = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 1:
                q.append((h, r, c))     # 익은 토마토 자리 저장

day = bfs()

if check_tomato():
    print(-1)
else:
    print(day)