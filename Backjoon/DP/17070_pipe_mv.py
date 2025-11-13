"""
backjoon_17070 - 파이프 옮기기 1 - G5

문제
- 집의 크기는 NxN의 격자판으로 나타낼 수 있고, 1x1크기의 정사각형 칸으로 나누어져 있다
- 각각의 칸은 (r,c)로 나타낼 수 있다. r은 행의 번호, c는 열의 번호, 모두 1부터 시작한다. 
- 파이프는 2개의 연속된 칸을 차지한다. 빈칸일 때만 이동할 수 있다.
- 파이프의 방향
    - 오른쪽인 경우 : 오른쪽, 대각선
    - 아래인 경우 : 아래, 대각선
    - 대각선 : 오른쪽, 아래, 대각선

출력
- (N,N)으로 이동시키는 방법의 수

풀이
- 일반적인 dfs와 달리 방향이 정해져 있고
- 원래 자리로 돌아올 일이 없기 때문에 방문여부 체크는 필요없다.
- 그 외에는 경우에 따라 빈칸 체크만 다르게 하면 된다.
- 가로는 1, 세로는 2, 대각선은 3으로 표시

- 시간초과 해결을 위한 DP설계
    - 방향에 따라 리스트를 만든다.
    - 방향으로 가기위해 필요한 값들을 더해준다.
    - 예시
        - 가로로 r, c에 도착하기 위한 경우 = 이전자리를 가로, 대각선으로 도착해야한다.
        - dp1[r][c] = dp1[r][c-1] + dp3[r][c-1]
    - 위와 같이 세로, 대각선도 식 세우자!
"""

def garo_check(r, c):
    # 가로로 올 수 있고, 인덱스가 넘어가지 않으면 업데이트
    if pipe[r][c] != 1 and c-1 >= 0:
        dp_garo[r][c] = dp_garo[r][c-1] + dp_cross[r][c-1]

def sero_check(r, c):
    # 세로로 올 수 있고, 인덱스가 넘어가지 않으면 업데이트
    if pipe[r][c] != 1 and r-1 >= 0:
        dp_sero[r][c] = dp_sero[r-1][c] + dp_cross[r-1][c]

def cross_check(r, c):
    # 대각으로 올 수 있고, 인덱스가 둘다 넘지 않으면 업데이트
    if pipe[r][c] != 1 and pipe[r][c-1] != 1 and pipe[r-1][c] != 1:
        if r-1 >= 0 and c-1 >= 0:
            dp_cross[r][c] = dp_garo[r-1][c-1] + dp_sero[r-1][c-1] + dp_cross[r-1][c-1]

N = int(input())
pipe = [list(map(int, input().split())) for _ in range(N)]

dp_garo = [[0 for _ in range(N)] for _ in range(N)]
dp_sero = [[0 for _ in range(N)] for _ in range(N)]
dp_cross = [[0 for _ in range(N)] for _ in range(N)]

dp_garo[0][1] = 1   # 가로 출발지점 1로 업데이트
for r in range(N):
    for c in range(2, N):
        garo_check(r,c)
        sero_check(r,c)
        cross_check(r,c)

print(dp_garo[N-1][N-1] + dp_sero[N-1][N-1] + dp_cross[N-1][N-1])


# def my_dfs(r, c, direction):
#     global cnt
    
#     if r == N - 1 and c == N - 1:
#         cnt += 1
#         return

#     # 가로 이동 (현재 가로 or 대각선일 때)
#     if direction == 1 or direction == 3:
#         if c + 1 < N and pipe[r][c + 1] == 0:
#             my_dfs(r, c + 1, 1)

#     # 세로 이동 (현재 세로 or 대각선일 때)
#     if direction == 2 or direction == 3:
#         if r + 1 < N and pipe[r + 1][c] == 0:
#             my_dfs(r + 1, c, 2)

#     # 대각선 이동 (모든 방향에서 가능)
#     if c + 1 < N and r + 1 < N:
#         if pipe[r + 1][c + 1] == 0 and pipe[r + 1][c] == 0 and pipe[r][c + 1] == 0:
#             my_dfs(r + 1, c + 1, 3)