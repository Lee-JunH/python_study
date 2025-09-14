"""
backjoon_15686 - 치킨 배달 - G5

문제
- NxN 크기의 도시가 있다. 각 칸은 빈칸, 치킨집, 집 중 하나이다.
- 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
- 도시의 치킨 거리는 모든 집의 치킨 거리 합이다
- M개의 치킨집을 골랐을 때 도시의 치킨 거리가 가장 작게 되는지 구하는 문제

풀이
- 집에서 가장 가까운 치킨집을 찾아서 거리를 저장하고
- 1인 지점에서 bfs를 통해 가까운 치킨집과의 거리를 구한다

- 일단 M개의 치킨집을 먼저 선택해야함.
- 그 치킨집에 대해서 계산

풀이시간
- 많~~~이 걸림
"""

from collections import deque

def backtrack(idx, cnt):
    global min_distance

    if cnt == M:
        dosi_dist = 0
        for h in home:
            dist = 1000
            for c in chick:
                dist = min(dist, abs(h[0] - chicken[c][0]) + abs(h[1] - chicken[c][1]))
            dosi_dist += dist
        min_distance = min(min_distance, dosi_dist)
        return
    
    # chicken에서 M개만 선택
    for i in range(idx, len(chicken)):
        chick.append(i)
        backtrack(i+1, cnt+1)
        chick.pop()
        
N, M = map(int, input().split())
chicken_map = [list(map(int, input().split())) for _ in range(N)]

chicken = []    # 치킨집 위치 저장
home = []       # 집 위치 저장
for i in range(N):
    for j in range(N):
        if chicken_map[i][j] == 2:  
            chicken.append((i,j))
        if chicken_map[i][j] == 1:
            home.append((i,j))

min_distance = float('inf')

chick = []
backtrack(0, 0)

print(min_distance)