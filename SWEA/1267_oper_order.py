"""
SWEA_1267 - 작업순서 - D6

문제
- V개의 작업이 있다. 어떤 작업은 특정 작업이 끝나야 시작할 수 있다.
- 사이클이 존재하지 않을 때 일을 끝낼 수 있는 작업 순서를 찾는 문제

풀이
- bfs를 하는 것과 비슷하게 진행한다.
- 단방향 간선들을 연결하여 저장한다.
- 자기 값으로 오는 방향이 없는 값들을 큐에 넣어 놓는다.(먼저 뺄것)
- 그리고 빼면서 뺀 값의 자식들도 확인하면서 쭉 진행한다.
"""

from collections import deque

T = 10
for case in range(T):
    V, E = map(int, input().split())
    nodes = list(map(int, input().split()))

    tree = [[] for _ in range(V+1)]
    count = [0] * (V+1)     # 나에게 연결된 부모 수 저장
    for i in range(0, E*2, 2):
        tree[nodes[i]].append(nodes[i+1])
        count[nodes[i+1]] += 1
    
    my_q = deque()
    for i in range(1, V+1):
        if count[i] == 0:
            my_q.append(i)
    
    result = []
    while my_q:
        cur = my_q.popleft()
        result.append(cur)
        for next in tree[cur]:
            count[next] -= 1
            if count[next] == 0:
                my_q.append(next)
    print(f'#{case+1}', end=' ')
    print(*result)