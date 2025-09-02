"""
SWEA_4408 - 자기방으로 돌아가기

문제
- 숙소는 긴 복도를 따라 400개의 방이 있다.
- 모든 학생들은 현재 위치에서 자신의 방으로 돌아가려고 하는데,
- 만약 두 학생이 자기방으로 돌아가면서 지나는 복도의 구간이 겹치면 두 학생은 동시에 돌아갈 수 없다.
- 최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지 구하시오.

풀이
- 복도의 길이는 200이고 출발지점부터 도착지점까지의 복도는 사용중으로 표시한다.
- 
"""

T = int(input())
for case in range(T):
    N = int(input())
    move = [list(map(int, input().split())) for _ in range(N)]

    corridor = [0 for _ in range(201)]
    for i in range(N):
        if move[i][0] % 2 == 0:
            start = move[i][0] // 2
        else:
            start = (move[i][0] + 1) // 2
        if move[i][1] % 2 == 0:
            end = move[i][1] // 2
        else:
            end = (move[i][1] + 1) // 2
        if start > end:
            temp = start
            start = end
            end = temp
        for j in range(start, end + 1):
            corridor[j] += 1
    print(f'#{case+1} {max(corridor)}')