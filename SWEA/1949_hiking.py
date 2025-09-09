"""
SWEA_1949 - 등산로 조성

문제
- NxN 높이를 나타낸 부지에서 최대한 긴 등산로를 만들 계획이다.
- 규칙
    - 등산로는 가장 높은 봉우리에서 시작
    - 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결
    - 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K깊이만큼 지형을 깎을 수 있다.
- 최대 공사 가능 깊이 K가 주어진다.

"""

def find_high():        # 가장 높은 곳 찾기
    max_high = 0
    for m in my_map:
        mm = max(m)
        max_high = max(max_high, mm)
    high_mountain = []
    for i in range(N):
        for j in range(N):
            if my_map[i][j] == max_high:
                high_mountain.append((i, j))
    return high_mountain

def dfs(r, c, way, gongsa):
    global max_way

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        if vis[nr][nc] == 1:
            continue
        if my_map[nr][nc] >= my_map[r][c]:        # 더 못가는데
            if gongsa == 1:     # 이미 공사했으면 다른 방향으로
                if max_way < way:
                    max_way = way
                continue
            if gongsa == 0:     # 공사 안했으면 공사 되는지 확인
                if max_way < way:
                    max_way = way
                if my_map[nr][nc] - K < my_map[r][c]:
                    gongsa = 1
                    temp = my_map[nr][nc]
                    my_map[nr][nc] = my_map[r][c] - 1
                    vis[nr][nc] = 1
                    dfs(nr, nc, way+1, gongsa)
                    vis[nr][nc] = 0
                    my_map[nr][nc] = temp
                    gongsa = 0
                    continue
                else:
                    continue
        vis[nr][nc] = 1
        dfs(nr, nc, way+1, gongsa) # 들어가잇
        vis[nr][nc] = 0


T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    high = find_high()
    
    max_way = 0
    while high:
        vis = [[0 for _ in range(N)] for _ in range(N)]
        r, c = high.pop()
        vis[r][c] = 1
        dfs(r, c, 1, 0)
    print(f'#{case+1} {max_way}')