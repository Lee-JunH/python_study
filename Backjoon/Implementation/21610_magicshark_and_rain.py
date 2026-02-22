"""
Backjoon_21610 - 마법사 상어와 비바라기

문제
- 비바라기 마법을 크기가 NxN인 격자에서 연습하려고 한다.
- 격자의 각 칸에는 바구니가 하나 있고 바구니에 저장할 수 있는 물의 양에는 제한이 없다.
- 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다.
- 즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있다.
- 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
- 이제 구름에 이동을 M번 명령하려고 한다.
- i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다.
    - 1. 모든 구름이 d방향으로 s칸 이동
    - 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니의 물이 1 증가
    - 3. 구름이 모두 사라짐
    - 4. 2에서 증가한 칸에 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 물 증가
        - 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    - 5. 바구니의 물 양이 2 이상인 모든 칸에 구름이 생기고, 물이 2 줄어든다.
        - 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
- M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합은?
"""

def move_clouds(d, s):  # 수학식으로 계산하자
    for r, c in clouds:
        nr = (r + (dir[d-1][0] * s)) % N
        nc = (c + (dir[d-1][1] * s)) % N
        moved.add((nr, nc))

def add_water():
    for r, c in moved:
        for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N or basket[nr][nc] == 0:
                continue
            basket[r][c] += 1

def generate_clouds():
    for i in range(N):
        for j in range(N):
            if (i,j) not in moved and basket[i][j] >= 2:
                clouds.append((i,j))
                basket[i][j] -= 2

def sum_water():
    total = 0
    for i in range(N):
        for j in range(N):
            total += basket[i][j]
    return total

N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for _ in range(M):
    d, s = map(int, input().split())
    moved = set()
    move_clouds(d, s)
    for r, c in moved:
        basket[r][c] += 1
    clouds = []
    add_water()
    generate_clouds()
print(sum_water())