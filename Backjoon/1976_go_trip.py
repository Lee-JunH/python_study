"""
Backjoon_1976 - 여행 가자 - G4

문제
- 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다.
- 여행경로가 주어졌을 때 이 여행 경로가 가능한지 알아보자.
- 다른 도시를 경유해서 할 수도 있다.

풀이
- 최소 신장 트리로 연결해서 여행 경로 값들을 확인한다!
"""

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
M = int(input())
nodes = [list(input().split()) for _ in range(N)]
plan_to_go = list(map(int, input().split()))

parent = [x for x in range(N)]

for i in range(N):
    for j in range(N):
        if nodes[i][j] == '0':
            continue
        if find(i) != find(j):
            union(i, j)

connect = parent[plan_to_go[0]-1]
result = 1
for plan in plan_to_go:
    if connect != parent[plan-1]:
        result = 0
        break
if result == 0:
    print('NO')
else:
    print('YES')