"""
Backjoon_1238 - 파티 - G3

문제
- N개의 구분된 마을이 있다.
- N명의 학생이 X번 마을에 모여서 파티를 한다.
- 이 마을 사이에는 총 M개의 단방향 도로들이 있다.
- 학생들은 파티에 참석했다가 다시 그들의 마을로 돌아온다.
- N명의 학생 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구인가

풀이
- 앞의 문제에서 만든 다익스트라 함수에서 출발점과 도착점을 추가해서 풀면 되겠따
- 갓다 왓다에 대한 정보를 저장하고 max출력하기!!
- 나이챠~
"""

from heapq import heappop, heappush

def dijkstra(num, arrive):
    if num == arrive:
        return 0
    
    vis = [float('inf')] * (N+1)
    heap = []
    heappush(heap, (0, num))     # K까지의 가중치가 작은 순으로 들어갈 것이다.
    # 가중치 부터 적어야 가중치에 대해서 비교됨!!
    
    while heap:
        time, cur = heappop(heap)
        if vis[cur] < time:
            continue
        for next, t in info[cur]:
            if time + t < vis[next]:
                vis[next] = time + t
                heappush(heap,(time+t, next))
    return vis[arrive]

N, M, X = map(int, input().split())
info = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    info[start].append((end, time))

person = [0] * (N+1)
for i in range(1, N+1):
    person[i] = dijkstra(i, X) + dijkstra(X, i)

print(max(person))