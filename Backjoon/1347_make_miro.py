"""
Backjoon_1347 - 미로 만들기 - S2

문제
- 미로 안의 한 칸에 남쪽을 보며 서있다.
- 미로는 직사각형 격자모양이고, 각 칸은 이동할 수 있거나, 벽을 포함하고 있다.
- 모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있다. 미로에서 모든 행과 열의 이동할 수 있는 칸을 걸어다녔다.
- 그러면서 자신의 움직임을 모두 노트에 쓰기로 했다. 미로의 지도를 자기 노트만을 이용해서 그리려고 한다.
- 'F'는 앞으로 한 칸 움직인 것이고, 'L'과 'R'은 방향을 왼쪽 또는 오른쪽으로 전환한 것이다.
- 첫째 줄에 미로 지도를 출력한다. '.'은 이동할 수 있는 칸이고, '#'는 벽이다.
"""

cnt = int(input())
word = input().strip()

dir = 1     # 동:0 남:1 서:2 북:3
map = [['#' for _ in range(101)] for _ in range(101)]
r = 50
c = 50
map[r][c] = '.'
right = 50
left = 50
up = 50
down = 50

for i in range(cnt):
    if word[i] == 'R':
        dir = (dir + 1) % 4
    elif word[i] == 'L':
        dir = (dir + 3) % 4
    else:
        if dir == 0:
            c += 1
        elif dir == 1:
            r += 1
        elif dir == 2:
            c -= 1
        elif dir == 3:
            r -= 1
        right = max(right, c)
        left = min(left, c)
        up = min(up, r)
        down = max(down, r)
        map[r][c] = '.'

for i in range(up, down + 1):
    for j in range(left, right + 1):
        print(map[i][j], end='')
    print()