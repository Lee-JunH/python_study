"""
SWEA_22683 - 나무 베기 - D3

문제
- RC카와 연결되는 문제
- 출발지에서 목적지까지 최단 거리가 아닌 최소 조작 횟수로 이동시킬 수 있다.
- 벨 수 있는 나무의 수가 주어졌을 때, 최소 조작 횟수를 구하는 문제

풀이
- 기존에는 거리를 저장했다면 이번엔 조작횟수를 저장하면서 나가자
- 근데 다른 방향으로 도착하는 경우가 존재할 수 있다.
"""

from collections import deque

def find_position(pos):
    for i in range(N):
        for j in range(N):
            if field[i][j] == pos:
                return (i,j)

def move(a, b, d):
    if d == 0:      #up
        if a - 1 >= 0 and field[a-1][b] != 'T':
            return (a-1, b)
    elif d == 1:    #right
        if b + 1 < N and field[a][b+1] != 'T':
            return (a, b+1)
    elif d == 2:    #down
        if a + 1 < N and field[a+1][b] != 'T':
            return (a+1, b)
    elif d == 3:    #left
        if b - 1 >= 0 and field[a][b-1] != 'T':
            return (a, b-1)
    return (a, b)

def bfs():
    global min_control

    my_q = deque([(start_r, start_c, 0)])
    visited = [[[0 for _ in range(K)] for _ in range(N)] for _ in range(N)]
    visited[start_r][start_c] = [1] * K

    while my_q:
        r, c, tree = my_q.popleft()
        if r == end_r and c == end_c:
            min_control = min(min_control, visited[r][c][tree])

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc][tree] != 0:
                continue
            if field[nr][nc] == 'T':
                if tree == K-1:
                    continue
                else:
                    visited[nr][nc][tree+1] = visited[r][c][tree] + 1
                    my_q.append((nr, nc, tree+1))
            else:
                visited[nr][nc][tree] = visited[r][c][tree] + 1
                my_q.append((nr, nc, tree))

T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    field = [list(input().strip()) for _ in range(N)]

    start_r, start_c = find_position('X')   # 출발 지점
    end_r, end_c = find_position('Y')       # 도착 지점

    dr = [0, 1, 0 ,-1]
    dc = [1, 0, -1, 0]
    min_control = float('inf')
    bfs()

    if min_control == float('inf'):
        print(-1)
    else:
        print(min_control)