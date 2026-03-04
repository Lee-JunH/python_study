"""
Programmers - 홀짝트리

문제
- 루트 노드가 설정되지 않은 1개 이상의 트리가 있습니다. 즉, 포레스트가 있습니다.
- 모든 노드들은 서로 다른 번호를 가지고 있습니다.
- 각 노드는 홀수 노드, 짝수 노드, 역홀수 노드, 역짝수 노드 중 하나입니다.
- 각 노드의 정의는 다음과 같으며, 0은 짝수입니다.
    - 홀수 노드 : 홀수고 자식 노드의 개수가 홀수
    - 짝수 노드 : 짝수고 자식 노드의 개수가 짝수
    - 역홀수 노드 : 홀수고 자식 노드의 개수가 짝수
    - 역짝수 노드 : 짝수고 자식 노드의 개수가 홀수
- 각 트리에 대해 루트 노드를 설정했을 때, 홀짝 트리가 될 수 있는 개수와 역홀짝 트리가 될 수 있는 개수를 구하려고 한다.
    - 홀짝 트리 : 홀수 노드와 짝수 노드로만 이루어진 트리
    - 역홀짝 트리 : 역홀수 노드와 역짝수 노드로만 이루어진 트리

조건
- 1 <= nodes의 길이 <= 400,000
    - 1 <= nodes의 원소 <= 1,000,000
- 1 <= edges의 길이 <= 1,000,000
    - edges의 원소는 [a, b] 형태의 1차원 정수 배열이며, a번 노드와 b번 노드 사이에 무방향 간선이 존재함을 의미한다.
    - a, b는 nodes에 존재하는 원소이며 서로 다르다.
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def check_child(my_nodes, node, vis, cnt):
    vis.add(node)

    # 홀수 노드
    if node % 2 == 1 and len(my_nodes[node]) % 2 == 1:
        cnt[0] += 1
    # 짝수 노드
    if node % 2 == 0 and len(my_nodes[node]) % 2 == 0:
        cnt[1] += 1
    # 역홀수 노드
    if node % 2 == 1 and len(my_nodes[node]) % 2 == 0:
        cnt[2] += 1
    # 역짝수 노드
    if node % 2 == 0 and len(my_nodes[node]) % 2 == 1:
        cnt[3] += 1
    
    for n in my_nodes[node]:    # 나머지 자식들도 확인
        if n in vis:
            continue
        check_child(my_nodes, n, vis, cnt)
    return

def solution(nodes, edges):
    my_nodes = defaultdict(set)

    for a, b in edges:      # 먼저 노드 연결
        my_nodes[a].add(b)
        my_nodes[b].add(a)

    sniffling = 0
    reverse_s = 0

    vis = set()
    for node in nodes:
        if node not in vis:
            vis.add(node)

            cnt = [0,0,0,0]
            check_child(my_nodes, node, vis, cnt)

            if cnt[0] + cnt[1] == 1:
                sniffling += 1
            if cnt[2] + cnt[3] == 1:
                reverse_s += 1

    return (sniffling, reverse_s)

nodes = [11, 9, 3, 2, 4, 6]
edges = [[9, 11], [2, 3], [6, 3], [3, 4]]
print(solution(nodes, edges))