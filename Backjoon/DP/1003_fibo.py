"""
Backjoon_1003 - 피보나치 함수 - S3

문제
- fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 문제

풀이
- fino[n] = fibo[n-1] + fibo[n-2] 를 이용한다.
"""

T = int(input())
for _ in range(T):
    N = int(input())

    dp = [() for _ in range(N+2)]
    dp[0] = (1, 0)
    dp[1] = (0, 1)
    for i in range(2, N+1):
        dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    print(dp[N][0], dp[N][1])


"""
# 인터넷 풀이
T = int(input())
for _ in range(T):
    N = int(input())
    a, b = 1, 0
    
    for i in range(N):
        a,b = b, a+b 
    print(a,b)
"""