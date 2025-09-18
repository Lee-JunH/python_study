"""
SWEA_1226 - 미로1 - D4

문제
- 16x16행렬의 형태로 만들어진 미로에서 흰색은 길, 노란색은 벽을 나타낸다.
- 미로의 시작점은 (1,1), 도착점은 (13,13)이다.
- 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 문제

풀이
- 출발점부터 dfs를 진행하여 (13,13)으로 갈 수 있는지를 확인한다.
"""

def dfs(r, c):
    global check

    if miro[r][c] == 3:
        check = 1

    if check == 1:
        return
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
            continue
        if visited[nr][nc] == 1 or miro[nr][nc] == 1:
            continue
        if check == 1:
            return
        visited[nr][nc] = 1
        dfs(nr, nc)

T = 10
for _ in range(T):
    case = int(input())
    miro = [list(map(int, input().strip())) for _ in range(16)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = [[0 for _ in range(16)] for _ in range(16)]
    check = 0
    dfs(1,1)

    print(f'#{case} {check}')