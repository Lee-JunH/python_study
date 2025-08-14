# baekjoon_2559 - 수열 - S3

N, K = map(int, input().split())
temp = list(map(int, input().split()))

current_sum = sum(temp[0:K])
max_sum = current_sum

for i in range(K, N):
    current_sum += temp[i]
    current_sum -= temp[i - K]
    max_sum = max(max_sum, current_sum)

print(max_sum)

# 시간초과 코드 - 시간 복잡도가 커 오래 걸린다.

# N, K = map(int, input().split())
# temp = list(map(int, input().split()))

# result = 0
# for i in range(N - K + 1):
#     lst = temp[i : i + K]
#     result = max(result, sum(lst))
# print(result)