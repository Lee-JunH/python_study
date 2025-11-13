"""
backjoon_14502 - 연구소 - G4

문제
- 바이러스의 확산을 막기 위해 연구소에 벽을 세우려고 한다.
- 연구소는 NxM 직사각형이고 빈칸, 벽으로 이루어져 있다.
- 바이러스는 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
- 새로 세울 수 있는 벽의 개수는 3개
- 벽을 세웠을 때 안전영역 크기의 최댓값을 구하는 문젲

풀이
- 일단 bfs를 하기 전에 주변에 열려있는 길이 몇 개인지 보고 3개보다 적으면 막기?
- 2에서 동서남북 자리로 이동한다.
- 이동한 자리 주변(대각선 포함)을 봤을 때 1이 있으면 1로 채우기
- 1이 없으면 2로 채우기

- 2부터 시작해 봤는데 안되는 경우가 많음
- 1부터는 어떻게 할지 모르겠음

- 결론 그냥 모든 경우 탐색

- 팁
    - 이중 리스트를 복사하는 경우 deepcopy가 안전하지만
    - 한 리스트씩 가져오는 게 더 빠름
"""
import sys
input = sys.stdin.readline

def bfs(temp):
    # 바이러스 위치
    temp_virus = deque(virus)
    cnt = 0
    while temp_virus:
        r, c = temp_virus.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:      # 인덱스 초과
                continue
            if temp[nr][nc] == 2 or temp[nr][nc] == 1:    # 벽이거나 바이러스면 다음
                continue
            temp[nr][nc] = 2
            temp_virus.append((nr, nc))
            cnt += 1
    return cnt

def backtrack(wall):
    global max_zero, zero

    if wall == 3:
        temp = [row[:] for row in lab]
        cnt = bfs(temp)
        max_zero = max(max_zero, zero - cnt - 3)
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                backtrack(wall + 1)
                lab[i][j] = 0

from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

virus = deque()
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i,j))
zero = sum(lst.count(0) for lst in lab)
max_zero = 0
backtrack(0)

print(max_zero)



"""
- 새로운 방법

from itertools import combinations

for seleted_partition in combinations(empty_place, 3):
  max_size = max(max_size, bfs(seleted_partition))
"""