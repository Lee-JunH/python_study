"""
2178 - 미로탐색
"""

from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

cnt = 1
my_q = deque([(0,0)])
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while my_q:
    r, c = my_q.popleft()
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
            continue
        if visited[nr][nc] or miro[nr][nc] == 0:
            continue
        visited[nr][nc] = visited[r][c] + 1
        my_q.append((nr, nc))
print(visited[N-1][M-1])