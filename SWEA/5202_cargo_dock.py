"""
SWEA_5202 - 화물 도크 - D3

문제
- 24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 있다.
- 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해
- 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
- 최대 몇 대의 화물차가 이용할 수 있는가
"""

def backtrack(cur, cnt):
    global max_cnt

    if cur == N-1:
        max_cnt = max(cnt, max_cnt)
        return
    
    for i in range(cur+1, N):
        if not vis[i] and time[cur][1] <= time[i][0]:
            vis[i] = 1
            backtrack(i, cnt+1)
            vis[i] = 0

T = int(input())
for case in range(T):
    N = int(input())

    time = []
    for _ in range(N):
        s, e = map(int, input().split())
        time.append((s,e))
    time.sort()

    max_cnt = 0
    for i in range(N):
        vis = [0 for _ in range(N)]
        backtrack(i, 1)
    
    print(f'#{case+1} {max_cnt}')