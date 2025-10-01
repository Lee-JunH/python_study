"""
Backjoon_7562 - 나이트의 이동 - S1

문제
- 체스판 위에 한 나이트가 놓여져 있다. 나이트가 이동하려는 칸이 주어질 때 나이트는 몇 번 움직이면 이 칸으로 이동 가능한가?

풀이
- 최단 경로 문제
"""

from collections import deque

def djsktra(start, end):
    r_e, c_e = end

    vis = [[0 for _ in range(N)] for _ in range(N)]
    vis[start[0]][start[1]] = 1
    my_q = deque([start])
    count = 0

    while my_q:
        cur = my_q.popleft()
        if cur == end:
            return count
        for dir in range(8):
            nr = cur[0] + dr[dir]
            nc = cur[1] + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if vis[nr][nc] == 1:
                continue
            vis[nr][nc] = 1
            my_q.append((nr, nc))
        count += 1


T = int(input())
for _ in range(T):
    N = int(input())
    start = tuple(input().split())
    end = tuple(input().split())

    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    djkstra(start, end)