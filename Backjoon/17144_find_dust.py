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

from collections import deque

def spread(d):
    fine_dust = deque(d)
    while fine_dust:
        r, c = fine_dust.popleft()
        for dir in range(dir):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:  # 인덱스 초과
                continue
            if room[nr][nc] == -1:  # 공기청정기
                continue

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 1. 초기 먼지 저장
dust = []
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            dust.append((i,j))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for time in range(T):
    spread(dust)

print(sum(dust) + 2)