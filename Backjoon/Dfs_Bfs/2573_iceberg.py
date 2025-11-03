"""
Backjoon_2573 - 빙산 - G4

문제
- 빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어든다.
- 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는
- 0이 저장된 칸의 개수 만큼 줄어든다. 단, 각 칸에 저장된 높이는 0보다 더 줄지 않는다.
- 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 문제

풀이
- 처음 시작이 한 덩어리니까 분리된 덩어리 개수를 세는 것은 하나가 다 녹은 경우만 실행하자.
- 나머지는 DFS로 동작 구현
"""

from collections import deque

def count_part():
    vis = [[0 for _ in range(M)] for _ in range(N)]
    part = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0 and vis[i][j] != 1:
                my_q = deque([(i, j)])
                vis[i][j] = 1
                while my_q:
                    r, c = my_q.popleft()
                    for dir in range(4):
                        nr = r + dr[dir]
                        nc = c + dc[dir]
                        if nr < 0 or nr >= N or nc < 0 or nc >= M:
                            continue
                        if iceberg[nr][nc] == 0 or vis[nr][nc]:
                            continue
                        vis[nr][nc] = 1
                        my_q.append((nr, nc))
                part += 1
    if part >= 2:
        return True
    else:
        return False

def melt_iceberg():
    new_iceberg = [[0 for _ in range(M)] for _ in range(N)]
    melt = False
    few = True
    for r in range(N):
         for c in range(M):
            sea = 0             # 주변 바다 수
            if iceberg[r][c] != 0:
                few = False
                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if iceberg[nr][nc] == 0:    # 바다인 경우
                        sea += 1
                new_iceberg[r][c] = iceberg[r][c] - sea
                if new_iceberg[r][c] <= 0:  # 0이 된게 있는지 확인
                    new_iceberg[r][c] = 0
                    melt = True
    return melt, new_iceberg, few

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

year = 0
while True:
    year += 1
    check, iceberg, few = melt_iceberg()
    if few:     # 2 덩어리 이상으로 분리되지 않으면 0 -> 즉 계속 했을 때 모두 0이면
        year = 0
        break
    if check:   # 다 녹은 빙산이 있는 경우만 체크
        if count_part():       # 덩어리가 3개 이상이면
            break

print(year)