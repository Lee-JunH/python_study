"""
backjoon_12865 - 평범한 배낭 - G5

문제
- 여행에 필요하다고 생각하는 N개의 물건이 있다.
- 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있다.
- 배낭에 최대 K만큼의 무게를 넣을 수 있을 때, 물건들의 가치 최댓값을 구하라.

풀이
- 무게 W인 물건들의 합이 K보다 작을 때 V합의 최댓값을 구해야 한다.
- 모든 경우의 수를 하면 시간이 오래 걸릴 것 같다. (A형도 시간 초과 났었음..)
- 근데 K = 3 인데 1 4, 2 3 처럼 작은 수가 더 큰 경우도 있다.
- 그냥 다 해보자 -> 또 시간초과 났엄

- 민재햄이 그러셨지. DP는 점화식을 찾는 문제라고..
- 점화식이란 큰 문제를 작은 문제로 나누어서 푸는 공식
- 수학적으로는 다음 항을 이전 항들로 표현하는 관계식
"""

N, K = map(int, input().split())    # 물품의 수 N, 무게 최대 K
baggage = [tuple(map(int, input().split())) for _ in range(N)]  # 무게 W, 가치 V


print(max_sum)


# 1. 비트마스트 -> 시간 초과
# max_sum = 0
# for i in range(1<<N):   # 모든 부분 집합
#     bag = []
#     for j in range(N):
#         if i & (1<<j):
#             bag.append(j)
#     sum_bag = 0
#     sum_v = 0
#     for num in bag: # 부분 집합의 무게 합 구하기
#         sum_bag += baggage[num][0]
#         sum_v += baggage[num][1]
#     if sum_bag <= K:    # 최대 무게보다 작거나 같으면
#         if max_sum < sum_v: # 가치합이 max값인지 확인
#             max_sum = sum_v
# print(max_sum)

# 2. 민경's 부분집합 이용 -> 시간초과
# def subset(index, sum_w, sum_v):
#     global max_sum

#     if index >= N:
#         return 0
#     if sum_w <= K:
#         if max_sum < sum_v:
#             max_sum = sum_v
    
#     subset(index+1, sum_w+baggage[index][0], sum_v+baggage[index][1])
#     subset(index+1, sum_w, sum_v)