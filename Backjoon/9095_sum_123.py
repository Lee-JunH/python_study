"""
backjoon_9095 - 1,2,3 더하기 - S3

문제
- 정수 4를 1,2,3의 합으로 나타내는 방법은 총 7가지 있다. 1111, 112, 121, 211 ...
- 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
- 정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 문제

풀이
- n의 범위가 1~10이다.
    1. 시간제한이 1초지만 백트랙킹도 가능할 것 같다.

    2. DP로 풀어보자
        - 1*x + 2*y + 3*z = n 을 이용해보자.

풀이시간
- 6분
- 17분
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def johap(x, y, z):   # n개의 수를 조합하는 경우의 수
    return factorial(x+y+z) // (factorial(x) * factorial(y) * factorial(z))

T = int(input())
for _ in range(T):
    n = int(input())

    cnt = 0
    for x in range(n//1, -1, -1):
        for y in range(n//2, -1, -1):
            for z in range(n//3, -1, -1):
                if 1*x + 2*y + 3*z == n:
                    cnt += johap(x, y, z)
    print(cnt)

# def backtrack(num):
#     global cnt

#     if num == 0:
#         cnt += 1
#         return
#     if num < 0:
#         return

#     for i in range(3, 0, -1):
#         backtrack(num-i)

# T = int(input())
# for _ in range(T):
#     n = int(input())

#     cnt = 0
#     backtrack(n)

#     print(cnt)