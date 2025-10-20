"""
Backjoon_7562 - 나이트의 이동 - S1

문제
- 체스판 위에 한 나이트가 놓여져 있다. 나이트가 이동하려는 칸이 주어질 때 나이트는 몇 번 움직이면 이 칸으로 이동 가능한가?

풀이
- 최단 경로 문제
"""

from collections import deque

def dijkstra(start, end):
    r_s, c_s = start
    r_e, c_e = end

    vis = [[0 for _ in range(N)] for _ in range(N)]
    vis[r_s][c_s] = 1
    my_q = deque([start])

    while my_q:
        r, c = my_q.popleft()
        if r == r_e and c == c_e:
            break
        for dir in range(8):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if vis[nr][nc] != 0:
                continue
            vis[nr][nc] = vis[r][c] + 1
            my_q.append((nr, nc))
            if nr == r_e and nc == c_e:
                break
    return vis[r_e][c_e]

T = int(input())
for _ in range(T):
    N = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    dr = [-2, -1, 1, 2, 2, 1, -1, -2]   # 이동 가능 칸들
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    print(dijkstra(start, end) - 1)