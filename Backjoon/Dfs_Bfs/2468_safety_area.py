"""
Backjoon_2468 - 안전 영역 - S1

문제
- 높이 정보를 조사하여 비가 내렸을 때 잠기지 않는 안전 영역이 최대 몇개인지 조사하려 한다.
- 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
- 물에 잠기지 않는 안전한 영역은 물에 잠기지 않는 지점들이 동서남북으로 인접해 있으며
   그 크기가 최대인 영역을 말한다.
"""

from collections import deque

def bfs(i, j, new_vis):
   my_q = deque()
   my_q.append((i, j))
   new_vis[i][j] = 1

   dr = [0, 1, 0, -1]
   dc = [1, 0, -1, 0]
   while my_q:
      r, c = my_q.popleft()
      for dir in range(4):
         nr = r + dr[dir]
         nc = c + dc[dir]
         if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
         if new_vis[nr][nc] or vis[nr][nc]:
            continue
         new_vis[nr][nc] = 1
         my_q.append((nr, nc))

def count_safety():
   safety = 0
   new_vis = [[0 for _ in range(N)] for _ in range(N)]
   for i in range(N):
      for j in range(N):
         if vis[i][j] == 0 and new_vis[i][j] == 0:
            bfs(i, j, new_vis)
            safety += 1
   return safety

N = int(input())
rain = [list(map(int, input().split())) for _ in range(N)]

max_rain = 0
for i in range(N):
   r = max(rain[i])
   max_rain = max(r, max_rain)

max_safety = 1
for be in range(1, max_rain):
   vis = [[0 for _ in range(N)] for _ in range(N)]
   for i in range(N):
      for j in range(N):
         if rain[i][j] <= be:
            vis[i][j] = 1  # 잠긴 부분 체크
   max_safety = max(max_safety, count_safety())

print(max_safety)