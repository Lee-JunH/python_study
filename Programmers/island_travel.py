"""
Programmers - 무인도 여행

문제
- 격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있다.
- 지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타낸다.
- 지도의 각 칸에 적힌 숫자는 식량을 나타내는데, 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은
    해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냄
- 어떤 섬으로 놀러 갈지 못 정한 메리는 우선 각 섬에서 최대 며칠씩 머물 수 있는지 알아본 후 놀러갈 섬을 결정하려 한다.

출력
- 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return
- 만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return
"""

from collections import deque

def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    for i in range(N):
        maps[i] = list(maps[i])

    vis = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not vis[i][j] and maps[i][j] != 'X':
                my_q = deque([(i,j)])
                vis[i][j] = 1
                island = int(maps[i][j])
                
                while my_q:
                    r, c = my_q.popleft()
                    for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                        nr = r + dr
                        nc = c + dc
                        if nr < 0 or nr >= N or nc < 0 or nc >= M:
                            continue
                        if vis[nr][nc] or maps[nr][nc] == 'X':
                            continue
                        vis[nr][nc] = 1
                        my_q.append((nr, nc))
                        island += int(maps[nr][nc])
                answer.append(island)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer