"""
11725 - 트리의 부모 찾기
"""
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    my_q = deque()
    my_q.append(1)
    visited[1] = 1
    while my_q:
        idx = my_q.popleft()
        for n in tree[idx]:
            if not visited[n]:
                visited[n] = 1
                parent[n] = idx
                my_q.append(n)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0 for _ in range(N+1)]
parent = [0 for _ in range(N+1)]
bfs()

for i in range(2, N+1):
    print(parent[i])