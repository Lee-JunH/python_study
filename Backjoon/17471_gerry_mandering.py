"""
backjoon_17471 - 게리맨더링 - G3

문제
- N개의 구역이 있다. 이 구역을 두 개의 선거구로 나눠야 한다.
- 선거구에 포함된 구역은 모두 연결되어 있어야 한다.
- 두 선거구에 포함된 인구의 차이가 최소가 되도록 만드는 문제

풀이
- 먼저 구역들을 노드로 연결한다.
- 가능한 조합들을 만들고 그 조합을 가지고 선거구를 만든다.
- 그리고 선거구가 연결되있는지 확인
- 차이 저장

풀이 시간 : 2시간
"""

from collections import deque

def bfs_connect(lst):
    my_q = deque()
    my_q.append(lst[0])
    vis = [0] * (N+1)
    vis[lst[0]] = 1
    cnt = 1
    while my_q:
        start = my_q.popleft()
        for n in node[start]:
            if vis[n] or n not in lst:
                continue
            vis[n] = 1
            cnt += 1
            my_q.append(n)
    return cnt == len(lst)

def backtrack(idx):
    global min_dif

    if 1 <= len(area1) <= N//2:
        area2 = [n for n in range(1, N+1) if n not in area1]
        if bfs_connect(area1) and bfs_connect(area2):
            sum1 = 0
            sum2 = 0
            for i in area1:
                sum1 += population[i]
            for j in area2:
                sum2 += population[j]
            min_dif = min(min_dif, abs(sum1-sum2))
    
    if idx > N:
        return
    
    for i in range(idx, N+1):
        area1.append(i)
        backtrack(i+1)
        area1.pop()
                

N = int(input())
population = [0] + list(map(int, input().split()))
node = [[] for _ in range(N+1)]
for i in range(1, N+1):
    connection = tuple(map(int, input().split()))
    for j in range(1, connection[0]+1):
        node[i].append(connection[j])

min_dif = 1000

area1 = []
backtrack(1)

if min_dif == 1000:
    print(-1)
else:
    print(min_dif)