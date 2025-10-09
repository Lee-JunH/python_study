"""
Backjoon_1149 - RGB거리 - S1

문제
- RGB거리에는 집이 N개 있다. 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
- 칠하는 비용이 주어졌을 때, 집을 칠하는 최소비용을 구하는 문제
    - 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
    - N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
    - i번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
"""

N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = price[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2]

print(min(dp[N-1]))