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
- 3차원으로 저장하고 움직이기
"""

from collections import deque

def bfs():
    global min_distance

    my_q = deque([(0,0,0)])
    visited[0][0][0] = 1
    visited[0][0][1] = 1
    while my_q:
        r, c, wall = my_q.popleft()
        if r == N-1 and c == M-1:
            min_distance = min(min_distance, visited[r][c][wall])
            continue
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc][wall] != 0:
                continue
            if my_map[nr][nc] == 1:
                if wall == 1:
                    continue
                visited[nr][nc][1] = visited[r][c][wall] + 1
                my_q.append((nr, nc, 1))
            else:
                visited[nr][nc][wall] = visited[r][c][wall] + 1
                my_q.append((nr, nc, wall))

N, M = map(int, input().split())
my_map = [list(map(int, input().strip())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

min_distance = float('inf')
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

bfs()

if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)