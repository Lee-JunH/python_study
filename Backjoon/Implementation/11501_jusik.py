"""
backjoon_11501 - 주식 - S2

문제
- 미래를 예측하여 주가를 예상할 수 있다.
- 날 수가 주어지고 주가가 주어질 때 최대 이익을 구하는 문제이다.

풀이
- 가장 큰 값을 찾아서 그 앞의 값들과의 차를 더한다.
- 이후 인덱스 부터 큰 값을 찾아 계속 진행한다.
- 이건 시간초과

풀이2
- 뒤에서부터 max값을 갱신하면 된다!
- 그럼 불필요한 반복문이 필요없게된다.
- max보다 작은게 뒤에 있으면 안더해도 되는걸 이용
"""

T = int(input())
for case in range(T):
    N = int(input())
    jusik = list(map(int, input().split()))

    profit = 0
    max_j = 0
    for i in range(N-1, -1, -1):
        if jusik[i] > max_j:
            max_j = jusik[i]
        else:
            profit += max_j - jusik[i]
    print(profit)


# T = int(input())
# for case in range(T):
#     N = int(input())
#     jusik = list(map(int, input().split()))

#     i = 0
#     profit = 0
#     max_j = max(jusik[i:])
#     for i in range(N):
#         if jusik[i] == max_j:
#             if i == N-1:
#                 break
#             max_j = max(jusik[i+1:])
#             continue
#         profit += max_j - jusik[i]
#     print(profit)