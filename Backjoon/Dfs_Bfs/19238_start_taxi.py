"""
Backjoon_19238 - 스타트 택시 - G2

문제
- 손님을 도착지에 내려주면 연료가 충전된다. 연료가 바닥나면 업무가 끝난다.
- M명의 승객을 태우는 것이 목표이다.
- NxN 크기의 격자로 각 칸은 비어 있거나 벽이 놓여 있다.
- 택시는 항상 최단경로로만 이동한다. -> BFS

- 승객을 고를 때는 현재 위치에서 가장 가까운 승객을 고른다.
    - 그런 승객이 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다.
- 연료는 한 칸 이동할 때 1만큼 소모. 승객을 성공적으로 이동시키면, 소모한 양의 두배가 충전.
- 이동하는 중에 바닥나면 실패.

출력
- 데려다 줄 수 있는 경우 최종적으로 남는 연료의 양을 출력
- 데려다 줄 수 없는 경우 -1 출력

풀이
- 승객을 찾는 BFS와 승객 지점에서 도착지점까지 가는 BFS 2가지를 구현해보자
- bfs를 진행하면서 거리도 계산하고 연료도 계산 추가해야 함
- 1번 승객은 1번 도착지로 가는 것 잊지 말기
"""

from collections import deque

def find_passenger(a, b):
    my_q = deque()
    my_q.append((a, b))
    vis = [[0 for _ in range(N)] for _ in range(N)]
    vis[a][b] = 1
    while my_q:
        r, c = my_q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 인덱스 초과 넘어가기
                continue
            if my_map[nr][nc] == 1 or vis[nr][nc] != 0: # 벽이거나 방문한 경우 넘어가기
                continue
            vis[nr][nc] = vis[r][c] + 1
            my_q.append((nr, nc))

            if 0 < my_map[nr][nc] <= 400:  # 택시에서 가장 가까운 승객을 찾은 경우 리턴
                return nr, nc, vis[nr][nc]-1    # 승객 좌표와 사용 연료 리턴
    return -1, -1, -1

def find_goal(c, d):
    my_q = deque()
    my_q.append((c, d))
    vis = [[0 for _ in range(N)] for _ in range(N)]
    vis[c][d] = 1
    while my_q:
        r2, c2 = my_q.popleft()
        for dir in range(4):
            nr = r2 + dr[dir]
            nc = c2 + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 인덱스 초과 넘어가기
                continue
            if my_map[nr][nc] == 1 or vis[nr][nc] != 0: # 벽이거나 방문한 경우 넘어가기
                continue
            vis[nr][nc] = vis[r2][c2] + 1
            my_q.append((nr, nc))

            if my_map[nr][nc] == my_map[c][d] + 400:  # 승객의 목적지 도착 시 리턴
                return nr, nc, vis[nr][nc]-1    # 도착 지점 좌표와 사용 연료 리턴
    return -1, -1, -1


N, M, total_fuel = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(N)]

taxi_r, taxi_c = map(int, input().split())  # 택시의 첫 시작점
taxi_r -= 1
taxi_c -= 1
# 지도에 고객과 도착점 적어 놓기 2 -> 20, 3 -> 30
for i in range(M):
    start_r, start_c, end_r, end_c = list(map(int, input().split()))
    my_map[start_r-1][start_c-1] = i+2
    my_map[end_r-1][end_c-1] = i+2 + 400

dr = [-1, 0, 0, 1]  # 위, 좌, 아래, 우
dc = [0, -1, 1, 0]

for i in range(M):
    passenger_r, passenger_c, use_fuel = find_passenger(taxi_r, taxi_c)
    if use_fuel == -1:
        total_fuel = -1
        break
    my_map[taxi_r][taxi_c] = 0
    total_fuel -= use_fuel
    if total_fuel <= 0:   # 사용연료가 더 크면 오류 출력
        break

    taxi_r, taxi_c, use_fuel = find_goal(passenger_r, passenger_c)
    if use_fuel == -1:
        total_fuel = -1
        break
    my_map[passenger_r][passenger_c] = 0
    if total_fuel < use_fuel:   # 사용연료가 더 크면 오류 출력
        total_fuel = -1
        break
    else:
        total_fuel = total_fuel - use_fuel + (use_fuel * 2)

if total_fuel == -1:
    print(-1)
else:
    print(total_fuel)