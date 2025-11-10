"""
Backjoon_14503 - 로봇 청소기 - G5

문제
- 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 문제
- 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다.
- 로봇 청소기 동작
    - 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    - 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        - 보는 방향 유지한 채로 후진할 수 있다면 후진하고 청소
        - 벽이라 후진할 수 없다면 작동을 멈춘다.
    - 3. 청소되지 않은 빈칸이 있는 경우
        - 반시계 방향으로 90도 회전
        - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸인 경우 한칸 전진
        - 1번으로 돌아감
"""

def check_dirty():
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= M or room[nr][nc] == 1:
            continue
        if room[nr][nc] == 0:
            return 1
    return 0

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

clean = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        clean += 1
    if check_dirty():   # 4 방향에 청소되지 않은 빈칸이 있는 경우
        for _ in range(4):
            d = (d + 3) % 4     # 방향 전환
            if room[r + dr[d]][c + dc[d]] == 0:     # 앞쪽이 청소되지 않은 빈칸인 경우
                r += dr[d]
                c += dc[d]
                break
    else:       # 4방향에 청소되지 않은 빈칸이 없는 경우
        back_r = r - dr[d]
        back_c = c - dc[d]
        if back_r < 0 or back_r >= N or back_c < 0 or back_c >= M or room[back_r][back_c] == 1: 
            break
        else:
            r = back_r
            c = back_c

print(clean)