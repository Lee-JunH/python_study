"""
Backjoon_12886 - 돌 그룹 - G4

문제
- 돌은 3개의 그룹으로 나누어져 있으며 각각의 그룹에는 돌이 A, B, C개 있다.
- 모든 그룹에 있는 돌의 개수를 같게 만들려고 한다.
    - 크기가 같지 않은 두 그룹을 고른다.
    - 돌의 개수가 작은 쪽을 X, 큰 쪽을 Y라 할 때
    - X에 있는 돌의 개수를 X+X개로, Y에 있는 돌의 개수를 Y-X로 만든다.
- 돌을 같은 개수로 만들 수 있으면 1, 아니면 0을 출려하는 문제

풀이
- 2개를 선택하는 경우는 3가지로 A,B B,C A,C 가 있다.
- 이 3가지에 대해 백트래킹, bfs?
"""

from collections import deque

def stone_group():
    my_stone = deque([(A,B,C)])

    vis = set()
    vis.add((A,B,C))

    while my_stone:
        s1, s2, s3 = my_stone.popleft()
        if s1 == s2 == s3:
            return 1
        for a, b, c in (s1,s2,s3), (s2, s3, s1), (s3, s1, s2):
            if a == b:
                continue
            elif a > b:
                big = a
                small = b
            else:
                big = b
                small = a
            
            if (a,b,c) not in vis:
                vis.add((big-small, small+small, c))
                my_stone.append((big-small, small+small, c))
    return 0

A, B, C = map(int, input().split())

stone = A + B + C

print(stone_group())