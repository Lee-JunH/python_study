"""
Backjoon_1197 - 최소 스패닝 트리 - G4

문제
- 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 문제
- MST는 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중 가중치의 합이 최소인 트리

풀이
- 크루스칼 알고리즘을 사용해서 풀자.
- 크루스칼은 시간초과 프림알고리즘 통과
- import하면 492ms, 안하면 2920ms
"""

import sys
input = sys.stdin.readline

import heapq
V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))  # 무방향 그래프

visited = [False] * (V+1)
result = 0

pq = [(0, 1)]

while pq:
    w, node = heapq.heappop(pq)
    if visited[node]:
        continue
    visited[node] = True
    result += w

    for nw, next_node in graph[node]:
        if not visited[next_node]:
            heapq.heappush(pq, (nw, next_node))

print(result)

# 크루스칼 알고리즘
# def find(x):
#     while parent[x] != x:
#         x = parent[x]
#     return x

# def union(a, b):
#     x = find(a)
#     y = find(b)
#     if x > y:
#         parent[x] = y
#     else:
#         parent[y] = x

# V, E = map(int, input().split())

# parent = [x for x in range(V+1)]    # 부모 값 자신으로 초기화

# nodes = []
# for _ in range(E):
#     a, b, w = map(int, input().split())
#     nodes.append((w, a, b))

# nodes.sort()

# result = 0
# for w, a, b in nodes:
#     if find(a) != find(b):
#         union(a, b)
#         result += w

# print(result)