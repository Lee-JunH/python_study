"""
Backjoon_10775 - 공항 - G2

문제
- 공항에는 G개의 게이트가 있으며 각각 1~G까지의 번호를 가지고 있다.
- 공항에는 P개의 비행기가 순서대로 도착할 예정이며,
- i번째 비행기를 1번부터 g번째 게이트 중 하나에 영구 도킹한다.
- 가장 많은 비행기를 도킹시키는 방법은?

풀이
- 1~g 중 어디에 놓느냐에 따라 개수가 달라진다.
- 확인해야 하는 경우의 수가 g * g * ... 10^5 반복
- 다른 규칙 찾기
- 1 2 3 4 3 2
"""

def find(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

def union(a, b):
    x = find(a)
    y = find(b)
    
    if x == y:
        return

G = int(input())
P = int(input())
g = []
for _ in range(P):
    g.append(int(input()))

parent = [x for x in range(G+1)]

