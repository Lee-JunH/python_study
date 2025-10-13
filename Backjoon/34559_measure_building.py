"""
Backjoon_34559 - 건물 측량 - G3

문제
- 땅과 건물이 그려져 있는 NxM 크기의 지도가 있다.
- 지도의 가장 왼쪽 위는 (1,1), 오른쪽 아래는 (N,M)이다.
- 건물 조건
    - 1로 표현된 칸
    - 0이지만 상하좌우 인접한 0으로 이동해 지도의 테두리에 도달할 수 없는 칸
- 임의의 두 좌표가 주어질 때, 만들어지는 직사각형 모양의 범위에 새 건물을 지을 수 있는지 확인하는 문제
- 이 직사각형에는 건물이 포함되지 않아야 한다.
- 건물을 지을 수 없는 경우 직사각형 내 건물의 개수도 출력

풀이
1. 0인데 건물인 지점 찾아서 채우기
2. 두 좌표안에 건물 개수 세기

- 이 2가지만 하면 된다.
- 1번에서 모든 0인 지점에서 하면 시간이 오래 걸리지 않을까? -> 당근 오래 걸릴것 같다.
- 옆에가 열려있는지를 끝에서부터 확인할까? -> dp처럼 풀어보자.
    - 상하좌우를 확인하고 뚫림 여부를 저장하자 -> (상하좌우)로
"""

def find_building():
    for i in range(1, N):
        for j in range(1, M):
            check = 0
            for dir in range(4):
                nr = i + dr[dir]
                nc = j + dc[dir]
                if my_map[nr][nc] == 1:     # 건물이 주변에 있으면
                    dp[nr][nc][dir] = 0     # 그쪽 방향은 막힘
                    continue
                if check == 0 and dp[nr][nc][dir] == 1:    # 뚫린 방향이 있으면
                    check = 1                   # 건물 안짓기
            if not check:
                my_map[nr][nc] = 1


N, M = map(int, input().split())
my_map = [list(map(int, input().strip())) for _ in range(N)]
Q = int(input())

dr = [-1, 1, 0, 0]  # 상하좌우 순서
dc = [0, 0, -1, 1]
# 지도 최신화 하기
dp = [[(1,1,1,1)] * M] * N
find_building()

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    building = 0

    for i in range(r1-1, r2):
        for j in range(c1-1, c2):
            if my_map[i][j] == 1:
                building += 1
    if building == 0:
        print('YES')
    else:
        print(f'No {building}')