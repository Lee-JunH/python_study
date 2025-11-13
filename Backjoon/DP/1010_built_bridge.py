"""
Backjoon_1010 - 다리 놓기 - S5

문제
- 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있다.
- 강의 서쪽에는 N개의 사이트, 동쪽에는 M개의 사이트가 있다.
- 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 개수만큼 다리를 짓는다.
- 다리끼리는 겹칠 수 없다.
"""

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(1, M+1):
        dp[1][i] = i
    
    # N이 2 이상일 때
    for i in range(2, N+1):
        for j in range(i, M+1):
            for k in range(j, i-1, -1):
                dp[i][j] += dp[i-1][k-1]
    print(dp[N][M])