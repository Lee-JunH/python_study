"""
SWEA_5189 - 전자카트 - D3

문제
- 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량
"""

def dfs(cur, hap, cnt):
    global min_battery

    if hap > min_battery:
        return
    if cnt == N:
        min_battery = min(min_battery, hap+battery[cur][0])
    for i in range(1, N):
        if not vis[i]:
            vis[i] = 1
            dfs(i, hap+battery[cur][i], cnt + 1)
            vis[i] = 0

T = int(input())
for case in range(T):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    vis = [0 for _ in range(N)]

    min_battery = float('inf')

    dfs(0, 0, 1)

    print(f'#{case+1} {min_battery}')