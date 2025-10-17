"""
Backjoon_10775 - 공항 - G2

문제
- 공항에는 G개의 게이트가 있으며 각각 1~G까지의 번호를 가지고 있다.
- 공항에는 P개의 비행기가 순서대로 도착할 예정이며,
- i번째 비행기를 1번부터 g번째 게이트 중 하나에 영구 도킹한다.
- 가장 많은 비행기를 도킹시키는 방법은?

풀이
- 1~g 중 어디에 놓느냐에 따라 개수가 달라진다.
1. 확인해야 하는 경우의 수가 g * g * ... 10^5 반복
    - 시간초과
2. 들어온 번호에 일단 채우기
    - 시간초과
3. g -> g-1의 루트라고 생각하기?
    - union - find 방법 이용하기
"""
import sys
input = sys.stdin.readline

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

G = int(input())
P = int(input())

parent = [x for x in range(G+1)]

plane = 0
for _ in range(P):
    gate = int(input())

    boarding_number = find(gate)

    if boarding_number == 0:
        break

    union(boarding_number, boarding_number-1)
    plane += 1

print(plane)