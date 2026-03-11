"""
Backjoon_18430 - 무기 공학 - G4

문제
- 공학자 길동이는 외부의 침략으로부터 마을을 지킬 수 있는 부메랑 무기를 개발하는 공학자다.
- 길동이는 부메랑 제작을 위한 고급 나무 재료를 구했다.
- 이 나무 재료는 NxM크기의 직사각형 형태이며 나무 재료의 부위마다 그 강도가 조금씩 다르다.
- 넓은 사각형 형태의 나무 재료를 잘라서 여러 개의 부메랑을 만들고자 한다.
- 부메랑은 항상 3칸을 차지하는 ‘ㄱ’모양으로 만들어야 한다.
- 부메랑의 중심이 되는 칸은 강도의 영향을 2배로 받는다.
- 나무 재료의 형태와 각 칸의 강도가 주어졌을 때, 길동이가 만들 수 있는 부메랑들의 강도 합의 최댓값을 출력하는 프로그램을 작성하시오.
- 단, 나무 재료의 크기가 작아서 부메랑을 하나도 만들 수 없는 경우는 0을 출력한다.
"""

def boomerang(r, c, power):
    global max_power

    if c == M:
        r += 1
        c = 0

    if r == N:
        max_power = max(max_power, power)
        return

    if visited[r][c] == 0:
        for dir in range(4):
            nr1 = r + dir1[dir][0]
            nc1 = c + dir1[dir][1]
            nr2 = r + dir2[dir][0]
            nc2 = c + dir2[dir][1]

            if 0 <= nr1 < N and 0 <= nc1 < M and 0 <= nr2 < N and 0 <= nc2 < M:
                if not visited[nr1][nc1] and not visited[nr2][nc2]:
                    visited[r][c] = 1
                    visited[nr1][nc1] = 1
                    visited[nr2][nc2] = 1

                    temp_power = 2 * woods[r][c] + woods[nr1][nc1] + woods[nr2][nc2]
                    boomerang(r, c + 1, power + temp_power)

                    visited[r][c] = 0
                    visited[nr1][nc1] = 0
                    visited[nr2][nc2] = 0
    # 방문 한 경우 다음
    boomerang(r, c+1, power)


N, M = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(N)]

dir1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir2 = [(1, 0), (0, -1), (-1, 0), (0, 1)]
visited = [[0 for _ in range(M)] for _ in range(N)]
max_power = 0

boomerang(0, 0, 0)

print(max_power)