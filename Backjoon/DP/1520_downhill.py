"""
Backjoon_1520 - 내리막길 - G3

문제
- 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 상하좌우 이웃한 곳끼리만 가능하다.
- 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다.
- 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수

풀이
- bfs는 안되니까 dp
- 자기 위치에서 주변 값을 봤을 때 0이 있고 작은 값이 있으면 체크
"""

def dfs(r, c):
    # 목적지에 도착했다면?
    if r == M-1 and c == N-1:
        return 1
    
    # 이미 계산한 적이 있다면?
    if dp[r][c] != -1:
        return dp[r][c]
    
    # 네 방향으로 이동하며 경로 수 합산
    dp[r][c] = 0
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if my_map[nr][nc] <= my_map[r][c]:
            dp[r][c] += dfs(nr, nc)
    
    return dp[r][c]

M, N = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(M)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dp = [[-1 for _ in range(M)] for _ in range(N)]

print(dfs(0,0))