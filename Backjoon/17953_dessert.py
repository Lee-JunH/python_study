"""
Backjoon_17953 - 디저트 - G5

문제
- 건강을 위해 디저트는 하루에 한 가지만 먹기로 정해 놓는다.
- 어느 날 '만족감'에 패턴이 있는 것을 알아낸다.
- 특정 주기마다 n번째 날에 먹는 특정 디저트의 만족감이 정해져 있는 것이 아니다.
- 디저트를 먹을 때 전날에 먹었던 것과 같은 것을 먹으면 만족감이 반으로 감소한다.
- 이러한 패턴이 주어졌을 때, 만족감의 최대값을 찾는다.

풀이
- 하나를 선택하고 다음을 봤을 때 무조건 큰 걸 선택한다고 좋은게 아니니까
완전탐색을 해보자
"""

N, M = map(int, input().split())
dessert = [list(map(int, input().split())) for _ in range(M)]

dp = [[0 for _ in range(M)] for _ in range(N)]

for j in range(M):
    dp[0][j] = dessert[j][0]    # 기본 값 채우기

for i in range(1, N):   # 
    for j in range(M):
        satisfaction = 0
        for k in range(M):
            if k != j:  # 전에 먹은거랑 다르면 그대로
                satis = dp[i-1][k] + dessert[j][i]
            else:   # 전에 먹은거랑 같으면 반
                satis = dp[i-1][k] + dessert[j][i] // 2
            satisfaction = max(satis, satisfaction)
        dp[i][j] = satisfaction
print(max(dp[N-1]))