"""
Backjoon_11726 - 2xn 타일링 - S3

문제
- 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 문제

풀이
- n에 대해서 1을 뺀 n-1을 채우는 개수 + 2를 뺀 n-2를 채우는 개수의 합과 같다.
- 즉 dp[n] = dp[n-1] + dp[n-2]
- 초기 값을 미리 설정하면 dp[1] = 1, dp[2] = 2
- 마지막에 10,007로 나누기 조심
"""

n = int(input())

dp = [0] * (n+1)

if n > 2:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n] % 10007)
else:
    print(n)