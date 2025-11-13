"""
backjoon_16236 - 아기상어 - G3

문제
- NxN 크기의 공간에 물고기 M마리, 아기 상어 1마리가 있다. 한칸에는 물고기가 최대 1마리 존재
- 가장 처음에 아기 상어의 크기는 2이고, 1초에 상하좌우로 한 칸씩 이동한다.
- 아기상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
- 크기가 같은 물고기는 먹을 수 없지만 그 물고기가 있는 칸은 지나갈 수 있다.

- 아기상어 이동 경로
    - 더 먹을 수 있는 물고기가 없으면 엄마 상어에게 도움 요청 엄마~~
    - 먹을 수 있는 물고기가 1마리면, 그 물고기 먹기
    - 1마리보다 많으면, 가장 가까운 물고기 먹기
        - 거리는 물고기 있는 칸으로 이동할 때, 지나는 칸의 최솟값
        - 거리가 가까운 물고기가 많으면, 가장 위, 가장 왼쪽 물고기 먹기
- 아기 상어의 이동은 1초, 물고기 먹는 시간은 없다.
- 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.

출력
- 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 먹을 수 있는지

풀이
- 가까운 물고기의 위치를 찾는게 중요할 거 같다.
"""

def find_babyshark():
    for i in range(N):
        for j in range(N):
            if fish[i][j] == 9:
                fish[i][j] = 0
                return i, j

# bfs 해서 가장 가까운 물고기 찾기
def find_fish(r, c, size):
    global time

    my_stack = deque()
    vis = [[0 for _ in range(N)] for _ in range(N)]

    my_stack.append([r,c])
    vis[r][c] = 1
    dr = [-1, 0, 0, 1]  # 가까운 물고기를 찾기 위해 위, 왼쪽, 오른쪽 아래 순으로 탐색
    dc = [0, -1, 1, 0]

    check = 0
    temp2 = 0
    while my_stack:
        temp = my_stack.popleft()
        for dir in range(4):
            nr = temp[0] + dr[dir]
            nc = temp[1] + dc[dir]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if vis[nr][nc] != 0 or fish[nr][nc] > size:    # size보다 큰 곳은 못 지나감
                continue
            if check == 0 and fish[nr][nc] != 0 and fish[nr][nc] < size: # 먹을 수 있는 물고기를 찾으면 그 자리 리턴
                check = 1
                temp2 = vis[temp[0]][temp[1]] + 1    # 처음 만났을 때가 최소
            vis[nr][nc] = vis[temp[0]][temp[1]] + 1
            my_stack.append([nr, nc])
    if temp2 == 0:
        return N, N, 0
    for i in range(N):
        for j in range(N):
            if vis[i][j] == temp2 and fish[i][j] != 0 and fish[i][j] < size:
                return i, j, temp2-1



from collections import deque

N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]

f_temp = 0
time = 0
shark_size = 2  # 처음 크기는 2
r, c = find_babyshark()     # 상어 위치

while True:
    fish_r, fish_c, temp = find_fish(r, c, shark_size)
    if temp != 0:
        time += temp
    if fish_r == N and fish_c == N:
        break
    r = fish_r
    c = fish_c

    # size 업데이트
    f_temp += 1
    if f_temp == shark_size:
        shark_size += 1
        f_temp = 0
    fish[r][c] = 0

if time == 0:
    print(0)
else:
    print(time)