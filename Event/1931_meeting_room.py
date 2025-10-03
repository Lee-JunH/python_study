"""
1931 - 회의실 배정
"""

import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
time.sort()
w
for i in range(N):
    cnt = 1
    end = time[i][1]
    j = i + 1
    while j < N:
        start = time[j][0]
        if end <= start:
            cnt += 1
            end = time[j][1]
            j += 1
        else:
            j += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)