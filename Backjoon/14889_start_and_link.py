"""
Backjoon_14889 - 스타트와 링크 - S1

문제
- 축구 인원은 N명이고 짝수다. 이제 N/2명으로 이루어진 스타트팀과 링크 팀으로 나눈다.
- 능력치 S는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력이다.
- 팀의 능력치는 S의 합이다.
- 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소인 경우 최솟값은?
"""

def make_johap(idx, team):
    global min_dif

    if team == N / 2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if vis[i] and vis[j]:
                    start += S[i][j]
                if not vis[i] and not vis[j]:
                    link += S[i][j]
        min_dif = min(min_dif, abs(start - link))
    else:
        for i in range(idx, N):
            if not vis[i]:
                vis[i] = 1
                make_johap(i+1, team+1)
                vis[i] = 0

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

vis = [0 for _ in range(N)]

min_dif = float('inf')

make_johap(0,0)

print(min_dif)