"""
Backjoon_14891 - 톱니바퀴 - G5

문제
- 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 있다.
- 톱니는 N극 또는 S극 중 하나를 나타내고 있다.
- 두 톱니바퀴의 맞닿은 부분이 같으면 회전하지 않고, 다르면 반대방향으로 회전한다.
= 최종 톱니바퀴의 상태를 구하는 문제 (N극은 0, S극은 1) (시계방향은 1, 반시계 -1)
"""

from collections import deque

def turning_cog(num, dir):
    if dir == 1:    # 시계방향 - 마지막꺼 빼고 처음으로
        cog[num-1].appendleft(cog[num-1].pop())
    else:           # 반시계방향 - 처음꺼 빼고 마지막으로
        cog[num-1].append(cog[num-1].popleft())

cog = [deque(list(map(int, input().strip()))) for _ in range(4)]
t = int(input())
turn = [list(map(int, input().split())) for _ in range(t)]

for c, d in turn:
    # 맞닿은 부분 확인 (1,3 - 2,7) (2,3 - 3,7) (3,3 - 4,7)
    check1 = (cog[0][2] != cog[1][6])
    check2 = (cog[1][2] != cog[2][6])
    check3 = (cog[2][2] != cog[3][6])
    turning_cog(c,d)
    if c == 1:
        if check1:
            turning_cog(2, -d)
            if check2:
                turning_cog(3, d)
                if check3:
                    turning_cog(4, -d)
    if c == 2:
        if check1:
            turning_cog(1, -d)
        if check2:
            turning_cog(3, -d)
            if check3:
                turning_cog(4, d)
    if c == 3:
        if check2:
            turning_cog(2, -d)
            if check1:
                turning_cog(1, d)
        if check3:
            turning_cog(4, -d)
    if c == 4:
        if check3:
            turning_cog(3, -d)
            if check2:
                turning_cog(2, d)
                if check1:
                    turning_cog(1, -d)
result = 0
for i in range(4):
    if cog[i][0]:
        result += 2 ** i
print(result)