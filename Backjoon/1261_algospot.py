"""
Backjoon_1261 - 알고스팟 - G4

문제
- 미로는 NxM 크기이며, 빈 방 또는 벽으로 이루어져 있다.
- 벽은 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면 빈 방과 동일한 방으로 변한다.
- 현재 (1,1)에 있는 알고스팟 운영진이 (N,M)으로 이동하려면 벽을 몇 개 부수어야 하는지 구하는 문제

풀이
- 최단거리를 구하고 그동안 지나간 1의 개수를 세면 되지 않을까?
- 최단거리가 아닌 최단 벽이니까 모든 경우에서 벽 개수가 적은 경우를 구하자

- 큐에 넣을 때 벽이면 현재까지의 벽 +1 해서 넣고 heapq로 pop을 하면 되겠다.
"""

from heapq import heappop, heappush

def dijkstra():
    while q:
        wall, row, col = heappop(q)
        if row == M-1 and col == N-1:
            return wall
        for dir in range(4):
            nr = row + dr[dir]
            nc = col + dc[dir]
            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue
            if vis[nr][nc] == 1:
                continue
            vis[nr][nc] = 1
            if miro[nr][nc] == 1:
                heappush(q, (wall+1, nr, nc))
            else:
                heappush(q, (wall, nr, nc))

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(M)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

vis = [[0 for _ in range(N)] for _ in range(M)]

q = [(0, 0, 0)]     # 벽, 행, 열
print(dijkstra())