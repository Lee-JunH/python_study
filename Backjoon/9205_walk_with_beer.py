"""
backjoon_9205 - 맥주 마시면서 걸어가기 - G5

문제
- 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다.
- 맥주 한 박스에는 맥주가 20개 들어있고 50미터를 가기 전 한 병씩 마신다.
- 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다.
- 하지만 박스에 들어있는 맥주는 20병을 넘을 수 없다.
- 도착할 수 있으면 happy, 아니면 sad를 출력

풀이
- 일단 최대 이동 가능 거리는 20 * 50으로 1000m 를 갈 수 있다.
- bfs로 모든 편의점들에 대해 갈 수 있는지를 확인하고
- 리턴 지점은 현재 위치에서 락페스티벌로 갈 수 있는지 확인!

시간 : 50분 ~ 1시간
"""

from collections import deque

def bfs():
    my_q = deque([(home_x, home_y)])
    check = [0] * n

    while my_q:
        r, c = my_q.popleft()
        if abs(r - rock_x) + abs(c - rock_y) <= 1000:   # 락으로 이동 가능하면 리턴
            print('happy')
            return
        for i in range(n):
            if not check[i]:
                next_gs_x, next_gs_y = gs25[i]
                if abs(r - next_gs_x) + abs(c - next_gs_y) <= 1000:   # 편의점으로 이동 가능한지 체크
                    check[i] = 1
                    my_q.append(gs25[i])
    print('sad')

T = int(input())
for _ in range(T):
    n = int(input())
    home_x, home_y = map(int, input().split())
    gs25=[]
    for _ in range(n):
        gs_x, gs_y = map(int, input().split())
        gs25.append((gs_x, gs_y))
    rock_x, rock_y = map(int, input().split())
    
    bfs()