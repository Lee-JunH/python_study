"""
Backjoon_2666 - 벽장문의 이동 - G5

문제
- n개의 같은 크기의 벽장들이 일렬로 부텅져 있고 벽장의 문은 n-2개만 있다.
- 한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(즉, 벽장이 열려있다면) 그 벽장 앞으로 움직일 수 있다.
- 풀어야 할 문제는 입력으로 주어지는 사용할 벽장의 순서에 따라서 벽장문을 이동하는 순서를 찾는 것이다.
- 이 때 이동횟수를 최소로 하여야 한다. 열려있는 벽장의 개수는 항상 2개이다.

풀이
- n번의 벽장을 열기 위해서 하는 동작 구현 방법
    - 어떤 벽장을 열어야 할 때 양쪽 방향으로 바라보고 가장 가까운 빈 칸을 찾는다.
    - 빈칸과의 차이가 작은 쪽이 닫혀야 하는 옷장이다.
    - 문제는 같은 경우
        - 양 쪽 모두 보는 방법 -> bfs 사용
        - 아니면 dP
"""

from collections import deque

def bfs():
    min_dist = float('inf')
    my_q = deque([(0, a, b, 0)])
    
    while my_q:
        cur, c1, c2, cnt = my_q.popleft()

        if cnt > min_dist:
            continue

        if cur == using:
            min_dist = min(min_dist, cnt)
            continue

        dist_c1 = abs(numbers[cur]-c1)
        dist_c2 = abs(numbers[cur]-c2)

        my_q.append((cur+1, numbers[cur], c2, cnt+dist_c1))
        my_q.append((cur+1, c1, numbers[cur], cnt+dist_c2))
    return min_dist

n = int(input())
a, b = map(int, input().split())
using = int(input())
numbers = [int(input()) for _ in range(using)]

print(bfs())