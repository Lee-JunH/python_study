"""
SWEA_5189 - 전자카트 - D3

문제
- 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량
- 
"""

from collections import deque

def bfs():
    global min_battery

    my_q = deque()
    my_q.append((start, 0))
    
    while my_q:
        cur, hap = my_q.popleft()

        if sum(vis) == N:
            min_battery = min(min_battery, hap)
        for i in range(N):
            if i == cur:
                continue
            if vis[i] != 1:
                vis[i] = 1
                my_q.append((i, hap+battery[cur][i]))


T = int(input())
for case in range(T):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    vis = [0 for _ in range(N)]
    vis[0] = 1

    start = 0
    min_battery = float('inf')

    bfs()

    print(f'#{case+1} {min_battery}')


# 3
# 3
# 0 18 34
# 48 0 55
# 18 7 0
# 4
# 0 83 65 97
# 82 0 78 6
# 19 19 0 82
# 6 34 94 0
# 5
# 0 9 26 85 42
# 14 0 84 31 27
# 58 88 0 16 46
# 83 61 94 0 17
# 40 71 24 38 0