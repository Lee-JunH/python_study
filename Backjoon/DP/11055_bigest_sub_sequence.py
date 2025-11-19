"""
Backjoon_11055 - 가장 큰 증가하는 부분 수열 - S2

문제
- 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하시오.
"""

N = int(input())
A = list(map(int, input().split()))

bigest = [1] * N
bigest[0] = A[0]
for i in range(1, N):
  for j in range(i):
    if A[j] < A[i]:
      bigest[i] = max(bigest[i], bigest[j] + A[i])
    else:
      bigest[i] = max(bigest[i], A[i])

print(max(bigest))