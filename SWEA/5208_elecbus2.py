"""
SWEA_5208 - 전기버스2 - D3

문제
- 충전지를 교환하는 방식의 전기버스를 운행하려 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고,
  충전지마다 최대로 운행할 수 있는 정류장의 수가 정해져 있다.
- 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 도착해야 한다.
- 목적지에 도착하는데 필요한 최소한의 교환횟수는?

풀이
- 먼저 충전 후 최대 이동거리로 가보고 안되면 돌아오는 백트래킹방식을 이용해보자
"""

# 정류장 번호, 배터리, 교환 횟수
def backtrack(stop, battery, cnt):
    global min_cnt

    for i in range(stop + battery, stop, -1):   # 최대 갈 수 있는 곳 부터 탐색
        if i >= N:   # 도착할 수 있으면 교환 횟수 업데이트
            min_cnt = min(min_cnt, cnt)
            return
        if cnt + 1 >= min_cnt:
            continue
        backtrack(i, M[i-1], cnt+1)

T = int(input())
for case in range(T):
    N, *M = map(int, input().split())

    min_cnt = N
    backtrack(1, M[0], 0)

    print(f'#{case+1} {min_cnt}')