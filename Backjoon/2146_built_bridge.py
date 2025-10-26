"""
Backjoon_2146 - 다리 만들기 - G3

문제
- 한 섬과 다른 섬을 잇는 다리를 가장 짧게 만들어 돈을 아끼려 한다.
- 지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 구하는 문제

풀이
- 섬의 주변 점들을 set으로 중복없이 저장해서 모든 점에서 bfs로 뻗어 가다가 어떤 1을 만났을 때
- 그 값이 다음 섬으로의 짧은 지점?
"""

from collections import deque

def bfs():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    new_q = deque(outline)
    while new_q:
        r, c, length = new_q.popleft()
        if length >= min_bridge:
            break
        visited[r][c] = 1
        for dr, dc in (0,1), (1,0), (0,-1), (-1,0):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if cur_vis[nr][nc] or visited[nr][nc]:
                continue
            if my_map[nr][nc] == 1:
                return length
            new_q.append((nr, nc, length+1))
            visited[nr][nc] = 1
    return length

def bfs_for_island(a, b):
    q = deque([(a, b)])
    island[a][b] = 1
    cur_vis[a][b] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in (0,1), (1,0), (0,-1), (-1,0):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if island[nr][nc]:
                continue
            if my_map[nr][nc] == 0: #테두리 저장하기
                outline.add((nr, nc, 1))
                continue
            island[nr][nc] = 1
            cur_vis[nr][nc] = 1
            q.append((nr, nc))

N = int(input())
my_map = [list(map(int, input().split())) for _ in range(N)]

min_bridge = float('inf')
island = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if my_map[i][j] == 1 and island[i][j] == 0: # 땅을 찾았고, 방문안한 섬인경우
            outline = set([])
            cur_vis = [[0 for _ in range(N)] for _ in range(N)]
            bfs_for_island(i, j)    # 연결된 땅 방문 체크하기 + 섬 인근 바다 리스트에 넣기
            new_bridge = bfs()      # 가까운 땅 찾기
            min_bridge = min(min_bridge, new_bridge)

print(min_bridge)