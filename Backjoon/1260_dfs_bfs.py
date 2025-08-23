"""
backjoon_1260 - DFS와 BFS - S2

문제
- 그래프를 DFS로  탐색한 결과와 BFS로 탐색한 결과를 출력
- 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
- 더 이상 방문할 수 있는 점이 없는 경우 종료
"""

# 이번 문제는 출력만 하면 되니까 스택사용 X
def dfs_v2(start):
        print(start, end=' ')
        visited[start] = True
        
        for child in node[start]:
            if not visited[child]:
                dfs_v2(child)
# bfs 함수 선언
def bfs():
    my_q = deque([V])
    vis = [False for _ in range(N+1)]
    vis[V] = True
    
    while my_q:
        temp = my_q.popleft()
        print(temp, end=' ')    # 큐에서 pop한 것 바로 출력
        
        for child in node[temp]:    # 노드의 자식 노드 확인
            if not vis[child]:
                vis[child] = True
                my_q.append(child)

import sys
input = sys.stdin.readline  # input함수를 이걸로 덮어쓰는 것이다.
from collections import deque

N, M, V = map(int, input().split())
node = [[] for _ in range(N+1)]

# 노드 양방향 연결 및 안의 값들 정렬
for _ in range(M):
    p, c = map(int, input().split())
    node[p].append(c)
    node[c].append(p)
for l in node:
    l.sort()

#1. dfs는 재귀를 사용하여 변수를 미리 선언
visited = [0 for _ in range(N+1)]	# 방문 여부 체크
dfs_v2(V)
print()
#2. bfs는 함수 내부에서 변수 선언
bfs()


# # dfs 함수 선언
# def dfs(stack):
#     while stack:
#         temp = stack.pop()
#         print(temp, end=' ')    # 스택에서 pop한 것 바로 출력
        
#         for child in node[temp]:
#             if not visited[child]:
#                 visited[child] = True
#                 stack.append(child)
#                 dfs(stack)
# my_stack = []
# my_stack.append(V)
# visited[V] = 1
# dfs(my_stack)
# visited = [0 for _ in range(N+1)]	# 방문 여부 체크
# bfs(my_stack)
