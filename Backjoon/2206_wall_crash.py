"""
backjoon_2206 - 벽 부수고 이동하기 - G3

문제
- NxM의 행렬로 표현되는 맵이 있다.
    - 0 : 이동 가능
    - 1 : 이동할 수 없는 벽
- (1,1) 에서 (N,M)까지 최단 경로로 이동하려 한다. (시작과 끝 포함)
- 벽을 하나 부수는 것도 가능하다.
- 불가능한 경우 -1 출력

풀이
- 일반적으로는 bfs를 사용하여 최소 거리를 찾을 수 있다.
- 하지만 벽을 한번 부수는 것이 가능하다.
- 그러면 벽을 부수는 경우가 다양하니까 백트래킹도 사용해야하나?
"""

def backtrack(r, c, dist, wall):
    global min_distance

    if r == N-1 and c == M-1:
        min_distance = min(min_distance, dist)
        return
    
    if dist >= min_distance:
        return

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc] != 0:
            continue
        if my_map[nr][nc] == 1 and wall == 0:
            visited[nr][nc] = 1
            backtrack(nr, nc, dist+1, 1)
            visited[nr][nc] = 0
            continue
        
        if my_map[nr][nc] == 1 and wall == 1:
            continue
        visited[nr][nc] = 1
        backtrack(nr, nc, dist+1, wall)
        visited[nr][nc] = 0

from collections import deque

def bfs(q, vis, wall):
    global min_distance

    new_vis = [row[:] for row in vis]
    while q:
        r, c = q.popleft()
        if new_vis[r][c] >= min_distance:
            return
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if new_vis[nr][nc] != 0:
                continue
            if my_map[nr][nc] == 1 and wall == 1:
                continue

            new_vis[nr][nc] = new_vis[r][c] + 1
            if my_map[nr][nc] == 1 and wall == 0:
                bfs(deque([(nr, nc)]), new_vis, 1)
                continue

            if nr == N-1 and nc == M-1:
                min_distance = min(min_distance, new_vis[nr][nc])
            q.append((nr, nc))

N, M = map(int, input().split())
my_map = [list(map(int, input().strip())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
min_distance = float('inf')

#my_q = deque()
#my_q.append((0,0))
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

#bfs(my_q, visited, 0)
backtrack(0, 0, 1, 0)

if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)