"""
Backjoon_1922 - 네트워크 연결 - G4

문제
- 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다.
- 최소 비용으로 컴퓨터를 연결하는 문제
"""

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x    

N = int(input())
M = int(input())

nodes = [list(map(int, input().split())) for _ in range(M)]

parent = [x for x in range(N+1)]

nodes.sort(key = lambda x:x[2])

result = 0
cnt = 0
for a, b, w in nodes:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        result += w
        if cnt == N-1:
            break
print(result)