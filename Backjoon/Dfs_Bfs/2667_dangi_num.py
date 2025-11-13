"""
backjoon_2667 - 단지번호붙이기 - S1

문제
- 1은 집이 있는 곳, 0은 집이 없는 곳이다.
- 좌우, 위, 아래로 연결된 집의 단지를 정의하고, 단지에 번호를 붙이려 한다.
- 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬.

출력
- 단지수와 각 단지 집의 수를 오름차순으로 정렬하여 출력

풀이
- 집을 입력 받고 집에 대해서 dfs를 실행한다.
- dfs를 실행하면서 최종 리스트에 개수를 입력하고 정렬 후 출력
"""

def dfs_home(r, c):
    global cnt

    if r < 0 or r >= N or c < 0 or c >= N:
        return
    if vis[r][c] or home[r][c] == 0:
        return
    vis[r][c] = 1
    cnt += 1
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        dfs_home(nr, nc)

N = int(input())
home = [list(map(int, input().strip())) for _ in range(N)]

vis = [[False for _ in range(N)] for _ in range(N)] # 방문 기록 저장
res_home = []   # 단지 별 집 수 저장
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 모든 점에 대해서 dfs 하여 개수 세기
for row in range(N):
    for col in range(N):
        if home[row][col] == 1 and not vis[row][col]:   # 집이고 방문 안한
            cnt = 0
            dfs_home(row, col)
            res_home.append(cnt)

dangi = len(res_home)
res_home.sort() # 정렬하여 출력
print(dangi)
for i in range(dangi):
    print(res_home[i])