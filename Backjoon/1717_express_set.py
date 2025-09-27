"""
Backjoon_1717 - 집합의 표현 - G5

문제
- n+1개의 집합 {0}, {1}, ..., {n}이 있다.
- 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산을 수행하려 한다.

풀이
- union, find 함수를 만드는 문제 같다.
"""

import sys
sys.setrecursionlimit(10**6)

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

n, m = map(int, input().split())
parent = [x for x in range(n+1)]
for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)
    elif op == 1:
        x = find(a)
        y = find(b)
        if x == y:
            print('YES')
        else:
            print('NO')