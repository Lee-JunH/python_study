"""
SWEA_1767 - 프로세서 연결하기 - SW Test 샘플문제

문제
- NxN개의 cell로 구성된 프로세서 멕시노스가 있다.
- 1개의 cell에는 1개의 Core 혹은 1개의 전선이 올 수 있다.
- 멕시노스의 가장자리에는 전원이 흐르고 있다.
- Core와 전원을 연결하는 전선은 직선으로만 설치가 가능하며, 전선은 절대 교차해서는 안된다.
- Core를 연결할 수 있는 최대한 많은 Core를 연결하는 방법을 찾고, 그 방법 중에서 전선의 길이가 가장 짧은 것을 찾는 문제
- 최대한 많은 Core에 전원을 연결했을 경우, 전선 길이의 합을 구하고자 한다.
- 단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.

풀이
- 먼저 코어를 찾는다.
- 코어를 끝으로 갈 수 있는지 확인한다.
- 갈 수 있으면 연결한다.
- 끝까지 가서 최소값에 저장하고 다시 돌아와서 다른방향으로도 헤본다.
- 즉 백트래킹? 완전탐색 문제
"""

# 직선 연결 가능 여부
def check_possible(r, c, d):
    nr = r + dr[d]
    nc = c + dc[d]
    while 0 <= nr < N and 0 <= nc < N:
        if cells[nr][nc] != 0:
            return False
        nr += dr[d]
        nc += dc[d]
    return True

def hyup_dfs(idx, wire, core):
    global total_wire, max_core

    if idx == len(cores):
        if core > max_core:
            max_core = core
            total_wire = wire
        elif core == max_core:
            total_wire = min(wire, total_wire)

        return

    i, j = cores[idx]

    for dir in range(4):
        nr = i + dr[dir]
        nc = j + dc[dir]
        if check_possible(i, j, dir):
            temp_r = nr
            temp_c = nc
            temp = 0
            # 전선 끝까지 가기
            while 0 <= temp_r < N and 0 <= temp_c < N:
                cells[temp_r][temp_c] = 2
                temp_r += dr[dir]
                temp_c += dc[dir]
                temp += 1
            hyup_dfs(idx + 1, wire + temp, core + 1)    
            # 전선 다시 되돌리기
            while 0 <= nr < N and 0 <= nc < N:
                cells[nr][nc] = 0
                nr += dr[dir]
                nc += dc[dir]
    hyup_dfs(idx+1, wire, core)


T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for case in range(T):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]
    cores = []

    for i in range(N):
        for j in range(N):
            if cells[i][j] == 1 and i != 0 and j != 0 and i != N-1 and j != N-1:
                cores.append((i,j))
    
    total_wire = float('inf')
    max_core = 0
    hyup_dfs(0, 0, 0)

    print(f'#{case+1} {total_wire}')