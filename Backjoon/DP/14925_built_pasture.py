"""
Backjoon_14925 - 목장 건설하기 - G4

문제
- 목장을 하나의 정사각형으로 최대한 크게 지으려고 하는데, 그 안에 나무나 바위는 없어야 한다.
- 땅의 세로 M미터, 가로 N미터일 때, 1미터 간격의 격자로 된 땅의 지도를 M x N행렬로 표현한다.
- 땅에서 지을 수 있는 가장 큰 정사각형 목장의 한 변의 크기 L을 구하는 문제

풀이
- 파리퇴치 같은 방법을 쓰면 너무 오래걸리니까 규칙이 있는 문제
- DP인걸 생각하고 풀면 이전 정보를 가지고 해결하는 방법
- dp[i][j]의 최대 크기는?
- 자기 위치의 최대 크기는 왼쪽, 왼쪽 위, 위의 3 값의 최소 값 + 1한 값
"""

M, N = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(M)]

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

max_length = 0

for i in range(1, M+1):
    for j in range(1, N+1):
        if field[i-1][j-1] != 0:
            dp[i-1][j-1] = 0
            continue
        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        max_length = max(max_length, dp[i][j])

print(max_length)