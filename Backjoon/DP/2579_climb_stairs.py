"""
Backjoon_2579 - 계단 오르기 - S3

문제
- 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
- 각 계단에는 일정한 점수가 쓰여 있다. 밟으면 점수를 얻게 된다.
- 계단 오르는 규칙
    - 계단은 한 번에 한 계단 또는 두 계단 가능.
    - 연속된 3개의 계단은 불가능.
    - 마지막 계단은 반드시 밟아야 함.
- 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 문제
"""

N = int(input())
stairs = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N)]

if N < 3:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
    print(dp[N-1])