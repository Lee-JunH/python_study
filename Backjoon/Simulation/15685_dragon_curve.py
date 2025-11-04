"""
Backjoon_15685 - 드래곤 커브 - G3

문제
- 드래곤 커브는 3가지 속성으로 이루어져 있다.
    - 시작 점
    - 시작 방향
    - 세대
- 0 세대 드래곤 커브는 길이가 1인 선분이다.
- 1 세대 드래곤 커브는 0세대 드래곤 커브를 끝 점을 기준으로
- 시계 방향으로 90도 회전시킨 다음 0세대 드래곤 커브의 끝 점에 붙인 것이다.
- 2 세대 드래곤 커브도 1세대를 만든 방법을 이용한다.
- 즉 K세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계방향 회전시킨 다음, 끝점에 붙인 것
- 드래곤 커브 N개가 있을 때 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수는?
- 0: 우, 1: 위, 2: 좌, 3: 아래

풀이
- 반복되는 방향들을 저장하고 방향에 따라 값 1로 바꾸고 사각형 개수 세기
"""

def count_square():
    count = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
                count += 1
    return count

def dragon_curve(gen):
    curve = [d]
    if gen >= 1:
        curve.append((d+1) % 4)
    for _ in range(1, gen):
        cnt = len(curve)
        for k in range(cnt): # 방향 반대로 바꿔주기
            if k < cnt // 2:
                curve.append((curve[k]+2) % 4)
            else:
                curve.append(curve[k])

    r, c = y, x
    for j in range(len(curve)):     # 채우기
        r += dr[curve[j]]
        c += dc[curve[j]]
        board[r][c] = 1

N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1
    dragon_curve(g)

print(count_square())