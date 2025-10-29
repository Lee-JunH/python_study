"""
Backjoon_1833 - 고속철도 - G3

문제
- N개의 도시로 이루어진 나라가 있다.
- 이 도시를 다니는 고속철도망을 만들어 도시간의 이동을 편하게 하려고 한다.
- 최소 비용으로 철도를 연결하는 문제
    - 단, 이미 설치된 철도가 존재한다.

풀이
- 최소 신장 트리에서 이미 설치된 것을 고려하여 진행한다.
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
rail = [list(map(int, input().split())) for _ in range(N)]

parent = [x for x in range(N)]
nodes = []

for i in range(N):
    for j in range(N):
        if rail[i][j] == 0:
            continue
        nodes.append((rail[i][j], i, j))

nodes.sort()

price = 0
new_nodes = []
cnt = 0
for new_rail, a, b in nodes:
    if new_rail < 0:
        if find(a) != find(b):
            union(a, b)
        price += -new_rail / 2
    else:

        if find(a) != find(b):
            price += new_rail
            union(a, b)
            new_nodes.append((a+1, b+1))
            cnt += 1
print(f'{int(price)} {cnt}')
for i in range(cnt):
    #print(f'{new_nodes[i][0]} {new_nodes[i][1]}')
    print(*new_nodes[i])