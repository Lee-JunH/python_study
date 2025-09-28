"""
Backjoon_1674 - 도시 분할 계획 - G4

문제
- 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져있다.
- 길은 양방향으로 다닐 수 있고, 유지비가 있다.
- 마을의 이장은 두 개의 분리된 마을로 분할한다.
- 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
- 나머지 길의 유지비의 합을 최소로 만드는 문제

풀이
- 첫번째로 N개의 집을 2개의 마을로 나누어야 한다.
    - 모든 경우의 수에 대해 해야하나?
- 두번째로 나눈 마을에 대해 MST를 만들어 최소로 이동할 수 있도록 한다.
    - 이거는 나눈 마을에 속하지 않은 집이면 다음 값으로 continue하기

- 최소신장트리는 최소로 연결되는 거니까 어차피 자르면 두개로 나뉜다!_!
- 최소 신장트리로 연결된 값중 가장 긴 것을 빼자!
"""

# import sys
# input = sys.stdin.readline

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

# def union(a, b):
#     x = find(a)
#     y = find(b)
#     if x != y:
#         if x > y:
#             parent[x] = y
#         else:
#             parent[y] = x
#         return True
#     return False

# N, M = map(int, input().split())
# way = [list(map(int, input().split())) for _ in range(M)]

# parent = [x for x in range(N+1)]

# way.sort(key=lambda x:x[2]) # 가중치 순으로 정렬해 놓기

# result = []     # 비용들을 리스트로 저장
# cnt = 0
# for a, b, price in way:
#     if union(a,b):
#         cnt += 1
#         result.append(price)
#         if cnt == N-1:
#             break
# print(sum(result) - max(result))


# prim Algirthm

import sys
input = sys.stdin.readline

from heapq import heappop, heappush, heapify
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]    # 간선 연결
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, a, b))
    graph[b].append((c, b, a))

# 1부터 시작
vis = [0 for _ in range(N+1)]

vis[1] = 1
my_heapq = graph[1]
heapify(my_heapq)
price = []  # 가중치 저장 리스트
cnt = 0

while my_heapq:
    p, start, end = heappop(my_heapq)
    if not vis[end]:
        vis[end] = 1
        price.append(p)
        cnt += 1
        if cnt == N-1:
            break
        for new in graph[end]:
            heappush(my_heapq, new)
print(sum(price) - max(price))