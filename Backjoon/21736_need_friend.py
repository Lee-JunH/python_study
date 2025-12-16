"""
Backjoon_21736 - 헌내기는 친구가 필요해 - S2

문제
- 대학의 캠퍼스는 NxM 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다.
- O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.
- 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하시오.
    - 아무도 만나지 못한 경우 TT를 출력
"""

# 1. BFS로 구현
from collections import deque

def bfs():
    cnt_person = 0
    while my_q:
        r, c = my_q.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if campus[nr][nc] == 'X' or vis[nr][nc]:
                continue
            if campus[nr][nc] == 'P':
                cnt_person += 1
            vis[nr][nc] = 1
            my_q.append((nr,nc))

    return cnt_person

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
vis = [[0 for _ in range(M)] for _ in range(N)]

my_q = deque()
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            my_q.append((i,j))
            vis[i][j] = 1

result = bfs()
if result == 0:
    print('TT')
else:
    print(result)

# # 2. DFS로 구현

# import sys
# sys.setrecursionlimit(10**6)

# def dfs(r, c):
#     global cnt_person

#     if r < 0 or r >= N or c < 0 or c >= M:
#         return

#     if campus[r][c] == 'X' or vis[r][c]:
#         return
    
#     if campus[r][c] == 'P':
#         cnt_person += 1

#     vis[r][c] = 1
#     dfs(r, c+1)
#     dfs(r+1, c)
#     dfs(r, c-1)
#     dfs(r-1, c)


# N, M = map(int, input().split())
# campus = [list(input().strip()) for _ in range(N)]

# vis = [[0 for _ in range(M)] for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if campus[i][j] == 'I':
#             start_r = i
#             start_c = j

# cnt_person = 0

# dfs(start_r, start_c)

# if not cnt_person:
#     print('TT')
# else:
#     print(cnt_person)