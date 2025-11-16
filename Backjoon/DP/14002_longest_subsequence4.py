"""
Backjoon_14002 - 가장 긴 증가하는 부분 수열4

문제
- 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 문제

풀이
- 자신보다 연속적으로 작은 값의 개수 계산하기
    - 이전 값들을 보면서 자신이 더 크면 그 값 +1 한 값과 자신의 값을 비교해서 저장
    - 이게 DP
"""

A_len = int(input())
A = list(map(int, input().split()))

bigger = [0 for _ in range(A_len)]
for i in range(A_len):
    for j in range(i):  # 어차피 i이후는 변경 안됐으니까 볼 필요 없음
        if A[i] > A[j]:
            bigger[i] = max(bigger[i], bigger[j]+1)
max_len = max(bigger)
result = []
for i in range(A_len-1, -1, -1):
    if bigger[i] == max_len:
        result.append(A[i])
        max_len -= 1
print(len(result))
print(*reversed(result))