"""
Backjoon_1753 - 최단경로 - G4

문제
- 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 문제

풀이
- 다익스트라 구현 
"""
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra():
    heap = []
    heappush(heap, (0, K))     # K까지의 가중치가 작은 순으로 들어갈 것이다.
                                # 가중치 부터 적어야 가중치에 대해서 비교됨!!
    while heap:
        way, cur = heappop(heap)
        if vis[cur] < way:
            continue
        for next, w in info[cur]:
            if way + w < vis[next]:
                vis[next] = way + w
                heappush(heap,(way+w, next))

V, E = map(int, input().split())    # 정점 수, 간선 수
K = int(input())                    # 시작 정점
node = [list(map(int, input().split())) for _ in range(E)]  # 간선 정보

info = [[] for _ in range(V+1)]     # 노드 연결
for u, v, w in node:
    info[u].append((v,w))

vis = [float('inf')] * (V+1)
vis[K] = 0
dijkstra()

for i in range(1, V+1):
    if vis[i] == float('inf'):
        print('INF')
    else:
        print(vis[i])