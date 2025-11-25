"""
Backjoon_2666 - 벽장문의 이동 - G5

문제
- n개의 같은 크기의 벽장들이 일렬로 부텅져 있고 벽장의 문은 n-2개만 있다.
- 한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(즉, 벽장이 열려있다면) 그 벽장 앞으로 움직일 수 있다.
- 풀어야 할 문제는 입력으로 주어지는 사용할 벽장의 순서에 따라서 벽장문을 이동하는 순서를 찾는 것이다.
- 이 때 이동횟수를 최소로 하여야 한다. 열려있는 벽장의 개수는 항상 2개이다.
"""

n = int(input())
a, b = map(int, input().split())
using = int(input())

closet = [1] * n
closet[a] = 0
closet[b] = 0
for _ in range(using):
    num = int(input())
     