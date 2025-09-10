"""
backjoon_18532 - 특정 거리의 도시 찾기 - S2

문제
- 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재, 도로의 거리는 1
- 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서
- 최단 거리가 정확히 K인 모든 도시들의 번호를 출력

풀이
1. 먼저 도시 정보를 입력받는다.
2. 출발 도시로 부터의 각 지점 까지의 최소 거리를 저장한다.
3. 거리가 K인 도시를 출력

풀이시간 : 20분 ~ 55분
"""

from collections import deque
import sys
input = sys.stdin.readline

def bfs(city_num):
    my_q = deque([city_num])
    distance = [-1] * (N+1)
    distance[city_num] = 0

    while my_q:
        cur = my_q.popleft()
        if distance[cur] == K:
            break
        for dosi in city[cur]:
            if distance[dosi] == -1:  # 더 짧게 갈 수 있으면 업데이트 X
                distance[dosi] = distance[cur] + 1
                my_q.append(dosi)
    return distance

N, M, K, X = map(int, input().split())

city = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    city[a].append(b)

distance = bfs(X)

dist = []
for i in range(1, N+1):
    if distance[i] == K:
        dist.append(i)

if dist:
    print("\n".join(map(str, dist)))
else:
    print(-1)


# import sys
# input = sys.stdin.readline

# def dfs(city_num, dist):
#     # 최소 거리 갱신
#     if dist == K:
#         distance[city_num] = min(distance[city_num], dist)
#         return
#     # 다음 도시로 이동
#     for dosi in city[city_num]:
#         dfs(dosi, dist+1)

# N, M, K, X = map(int, input().split())

# city = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     city[a].append(b)

# distance = [float('inf') for _ in range(N+1)]
# dfs(X, 0)

# dist = []
# for i in range(1, N+1):
#     if distance[i] == K:
#         dist.append(i)
# cnt = len(dist)
# if cnt == 0:
#     print(-1)
# else:
#     for i in range(cnt):
#         print(dist[i])