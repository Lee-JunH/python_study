"""
Backjoon_16987 - 계란으로 계란 치기 - G5

문제
- 삼대 오백 소연이는 문제를 틀릴 때 마다 턱걸이를 5회씩 한다.
- 계산으로 계란을 치게 되면 각 계란의 내구도는 상대 계란 만큼 깎이게 된다.
- 내구도가 0 이하가 되는 순간 계란은 깨진다.
- 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제
"""

def find_crack():
    cnt = 0
    for i in range(N):
        if egg[i][0] <= 0:
            cnt += 1
    return cnt

def backtrack(cur):
    global count

    if cur == N:      # 마지막 계란까지 확인한 경우
        count = max(count, find_crack())
        return

    if egg[cur][0] <= 0:  # 들고 있는 계란이 깨진 계란이면 다음
        backtrack(cur+1)
    else:
        check = 1
        for i in range(N):
            if cur == i:    # 자신과는 비교 X
                continue
            if egg[i][0] <= 0:  # 깨진계란과는 비교 X
                continue
            check = 0
            egg[cur][0] -= egg[i][1]    # 들고있는 계란 내구도 변화
            egg[i][0] -= egg[cur][1]    # 비교하고 있는 계란 내구도 변화
            backtrack(cur+1)
            egg[cur][0] += egg[i][1]
            egg[i][0] += egg[cur][1]

        if check:   # for문으로 한번도 안들어간 경우 (다 깨진 경우를 의미)
            backtrack(N)

N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]

count = 0
backtrack(0)

print(count)