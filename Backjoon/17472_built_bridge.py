"""
Backjoon_17472 - 다리 만들기 2 - G1

문제
- 섬으로 이루어진 나라가 있고, 모든 섬을 다리로 연결하려고 한다.
- 지도는 NXM 크기고, 격자의 각 칸은 땅이거나 바다이다.
- 다리는 바다에만 건설할 수 있고, 다리의 길이는 다리가 격자에서 차지하는 칸의 수이다.
- 다리는 직선으로만 건설할 수 있고, 다리의 길이는 2 이상이어야 한다.
- 다리는 다른 다리나 섬과 겹쳐질 수 없다.
- 모든 섬을 연결하는 다리 길이의 최솟값을 구하자.

풀이
- 먼저 섬을 나눈다. -> BFS
- 한 섬에서 다른 한 섬으로 이동하는 방법을 생각해본다.
    - 출발 도착 길이 로 값들을 저장한다.
- 저장한 값들을 트리를 이용해서 짧은 거리 합을 찾는다.
"""

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def check_island(r, c, n):
    my_q = deque()
    my_q.append((r, c))
    visited[r][c] = 1
    map[r][c] = n

    while my_q:
        cur = my_q.popleft()
        for dir in range(4):
            nr = cur[0] + dr[dir]
            nc = cur[1] + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc] or not map[nr][nc]:
                continue
            visited[nr][nc] = 1
            map[nr][nc] = n
            my_q.append((nr, nc))

def find_island(r, c, num, dir):
    # 상하좌우로 뻗어가서 다른 숫자가 있는지 체크
    nr = r + dr[dir]
    nc = c + dc[dir]
    dist = 0

    while 0 <= nr < N and 0 <= nc < M:
        if map[nr][nc] == num:
            break
        elif map[nr][nc] != 0 and map[nr][nc] != num:
            if dist >= 2:
                nodes.add((min(num, map[nr][nc]), max(num, map[nr][nc]), dist))
            break
        elif map[nr][nc] == 0:
            nr += dr[dir]
            nc += dc[dir]
            dist += 1

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

num = 1
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if map[i][j] and not visited[i][j]:
            check_island(i, j, num)
            num += 1

nodes = set()   #  중복 값이 있을 수 도 있으니까 set로 저장

for i in range(N):
    for j in range(M):
        if map[i][j]:
            find_island(i, j, map[i][j], 0)
            find_island(i, j, map[i][j], 1)
            find_island(i, j, map[i][j], 2)
            find_island(i, j, map[i][j], 3)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = x
        return True
    return False

parent = [i for i in range(num)]
edges = sorted(list(nodes), key=lambda x: x[2])

total_dist = 0
bridge_count = 0
islands = num - 1 # 전체 섬의 개수

for a, b, dist in edges:
    if union(a, b):
        total_dist += dist
        bridge_count += 1
        if bridge_count == islands - 1:
            break

if bridge_count == islands - 1:
    print(total_dist)
else:
    print(-1)