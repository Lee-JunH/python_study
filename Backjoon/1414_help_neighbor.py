"""
Backjoon_1414 - 불우이웃 돕기 - G3

문제
- N개의 방이 있다. 각 방에 1개의 컴퓨터가 있다.
- 각각의 컴퓨터는 랜선으로 연결되어 있다. 
- A와 B 컴퓨터가 랜선으로 연결되어 있거나 또 다른 컴퓨터를 통해 연결이 되어있으면 통신이 가능하다.
- N개의 컴퓨터를 모두 서로 연결되게 하고 싶다.
- N개의 컴퓨터가 서로 연결되어 있는 랜선의 길이가 주어질 때, 기부 가능 최댓값을 구하는 문제
    - a~z = 1~26, A~Z = 27~52

풀이
- 모든 노드를 연결하고 싸이클이 없고 최소합인 최소 스패닝 트리 문제이다.
- 프림 알고리즘이나 크루스칼 알고리즘으로 풀이하는 문제
"""

def find(x):    # 부모 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):    # a,b의 부모가 같은지 확인
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
data = [list(input().strip()) for _ in range(N)]

parent = [x for x in range(N+1)]
nodes = []

result = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == '0':
            nodes.append((0, i, j))
        else:
            if 'a' <= data[i][j] <= 'z':
                nodes.append((ord(data[i][j]) - ord('a') + 1, i, j))
                result += ord(data[i][j]) - ord('a') + 1
            elif 'A' <= data[i][j] <= 'Z':
                nodes.append((ord(data[i][j]) - ord('A') + 27, i, j))
                result += ord(data[i][j]) - ord('A') + 27

nodes.sort()     # 가중치 오름차순 정렬

cnt = 0
for lansun, x, y in nodes:
    if lansun == 0:
        continue
    if find(x) != find(y):
        union(x, y)
        result -= lansun
        cnt += 1

if cnt == N-1:
    print(result)
else:
    print(-1)