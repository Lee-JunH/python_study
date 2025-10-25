"""
Backjoon_1916 - 최소비용 구하기 - G5

문제
- N개의 도시가 있다. 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
- A번째 도시에서 B번째 도시까지 가는 비용을 최소화 시킬 때 최소비용은?

풀이
- 출발, 도착, 비용을 입력으로 주는 다익스트라 문제이다.
"""

from heapq import heappop, heappush

def dijkstra():
    my_heapq = [(0, start)]
    dist[start] = 0
    while my_heapq:
        cur_price, cur = heappop(my_heapq)
        for next, next_price in nodes[cur]:
            price = cur_price + next_price
            if dist[next] > price:
                dist[next] = price
                heappush(my_heapq, (price, next))

N = int(input())
M = int(input())

nodes = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, p = map(int, input().split())
    nodes[a].append((b, p))

start, end = map(int, input().split())

dist = [float('inf') for _ in range(N+1)]
dijkstra()
print(dist[end])