"""
SWEA_1486 - 장훈이의 높은 선반 - D4

문제
- 서점에는 높이가 B인 선반이 하나 있다.
- 각 점원의 키는 H 로 나타나는데 점원들이 탑을 쌓아서 선반 위 물건을 사용하기로 했다.
- 쌓는 탑은 점원 1명 이상으로 이루어져 있다.
- 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
- 탑의 높이가 B이상인 경우 선반 위의 물건을 사용할 수 있다.
- 높이가 높을수록 더 위험하므로 높이가 B이상인 탑 중에서 높이가 가장 낮은 탑을 알아내는 문제

풀이
- 합이 B이상이고 B와의 차이가 가장 작을 때의 차이를 구해야 한다.
"""

def dfs(hap, index):
    global min_cha

    if hap >= B:
        min_cha = min(min_cha, hap-B)
        return

    for i in range(index, N):
        if vis[i] == 1:
            continue
        vis[i] = 1
        dfs(hap+height[i], i)
        vis[i] = 0

T = int(input())
for case in range(T):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    min_cha = sum(height)
    vis = [0 for _ in range(N)]
    dfs(0, 0)

    print(f'#{case+1} {min_cha}')