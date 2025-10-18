"""
Backjoon_17144 - 미세먼지 안녕! - G4

문제
- 미세먼지를 제거하기 위해 공기청정기를 사용한다.
- 미세먼지는 모든 칸에서 동시에 확산이 일어난다.
    - 인접한 네방향으로 확산되고 확산되는 양은 A / 5 인 값이다.
    - 제자리에 남은 양은 A - A/5 * (확산 방향 수)
- 공기청정기의 바람으로 한 칸씩 이동한다.
    - 위쪽 바람은 반시계방향
    - 아래쪽 방향은 시계방향으로 순환된다.
    - 공기청정기로 들어간 미세먼지는 모두 정화된다.
- T초가 지난 후 남아있는 미세먼지의 양은?

풀이
- bfs를 하는 과정에서 확산 방향 수 계산과 공기청정기 바람을 추가해주면 될 것 같다.
"""

def spread(cur):
    fine_dust = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if cur[r][c] == -1:
                fine_dust[r][c] = -1
            elif cur[r][c] > 0:
                cnt = 0  # 퍼진 방향 수
                mini_dust = cur[r][c] // 5     # 퍼지는 먼지
                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C:  # 인덱스 초과
                        continue
                    if cur[nr][nc] == -1:  # 공기청정기
                        continue
                    cnt += 1
                    fine_dust[nr][nc] += mini_dust
                fine_dust[r][c] += cur[r][c] - mini_dust * cnt
    return fine_dust

def rotate(a, ud):
    r, c = (a,1)
    dir = 0
    prev = 0
    while True:
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            if ud == 'up':
                dir += 1    # 우 상 좌 하
            elif ud == 'down':
                dir = (dir+3) % 4   # 우 하 좌 상
            continue
        if nr == a and nc == 0:
            break
        prev, temp[r][c] = temp[r][c], prev
        r, c = nr, nc
    

def air_purifier():
    rotate(air, 'up')
    rotate(air+1, 'down')
    

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

dr = [0, -1, 0, 1]  # 우, 상, 좌, 하
dc = [1, 0, -1, 0]

for i in range(2, R):
        if room[i][0] == -1:
            air = i
            break

temp = room
for time in range(T):
    temp = spread(temp)
    air_purifier()

result = 0
for i in range(R):
    for j in range(C):
        if temp[i][j] > 0:
            result += temp[i][j]

print(result)