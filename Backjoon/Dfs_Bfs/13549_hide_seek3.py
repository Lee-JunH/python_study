"""
Backjoon_13549 - 숨바꼭질3 - G5

문제
- 수빈이는 현재 점 N에 있고 동생은 점 K에 있다.
- 위치가 X일 때, 1초 후 X-1 또는 X+1로 이동한다.
- 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
- 각자의 위치가 주어졌을 때 수빈이가 동생을 찾을 수 있는 가장 빠른 시간은?

풀이
- 경우는 3가지, X-1, X+1, 2*X 위치로 이동할 수 있다.
- 각 경우에 대해 bfs하기
- 대신에 가장 빠른 경우는 2*X인 경우니까 2*X는 가장 앞에 넣어주기 -> appendleft 이용
"""

from collections import deque

def bfs():
    global min_time

    my_q = deque()
    my_q.append((N, 0))     # 시작
    visited = [0] * 100001
    visited[N] = 1
    while my_q:
        cur, time = my_q.popleft()
        if cur == K:
            return time
        for new in (cur-1, cur+1, cur*2):
            if 0 <= new <= 100000 and visited[new] == 0:
                visited[new] = 1
                if new == cur * 2:  # 곱하기인 경우 가장 앞에 넣어주기
                    my_q.appendleft((new, time))    # 시간은 그대로
                else:
                    my_q.append((new, time+1))      # 시간 + 1

N, K = map(int, input().split())

print(bfs())


# from heapq import heappush, heappop

# def dijkstra():
#     if K <= N:
#         return(N-K)

#     heap = []
#     vis = [0] * 100001
#     vis[N] = 1
#     heappush(heap, [0,N])
#     while heap:
#         time, cur = heappop(heap)
#         if cur == K:
#             return time
#         for new in (cur-1, cur+1, cur*2):
#             if 0 <= new <= 100000 and vis[new] == 0:
#                 vis[new] = 1
#                 if new == cur * 2:
#                     heappush(heap, [time, new])
#                 else:
#                     heappush(heap, [time+1, new])

# N, K = map(int, input().split())

# print(dijkstra())