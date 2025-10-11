"""
Backjoon_16918 - 봄버맨 - S1

문제
- 봄버맨은 크기가 RxC인 직사각형 격자판 위에서 살고 있다.
- 폭탄이 있는 칸은 3초가 지난 후 폭발, 폭탄이 있던 칸이 파괴되어 빈칸이 되며, 인접한 네 칸도 함께 파괴된다.
- 인접한 칸에 폭탄이 있는 경우 폭발 없이 파괴된다.
- 봄버맨의 이동
    - 1초 동안 아무것도 하지 않는다.
    - 다음 1초 동안 폭탄이 설치되지 않은 모든 칸에 폭탄을 설치한다.
    - 1초가 지난 후 3초전에 설치된 폭탄이 모두 폭발한다.
    - 이를 반복
- N초가 흐른 후의 격자판 상태는?
"""

def fill_bomb():    # 폭탄 채우기
    for i in range(R):
        for j in range(C):
            if my_map[i][j] == 0:
                my_map[i][j] = 3

def minus_time():   # 1초 지난 결과
    bomb = []
    for i in range(R):
        for j in range(C):
            if my_map[i][j] != 0:
                my_map[i][j] -= 1
                if my_map[i][j] == 0:
                    bomb.append((i,j))  # 터진 자리 저장
    return bomb

R, C, N = map(int, input().split())
bomb = [list(input().strip()) for _ in range(R)]

my_map = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if bomb[i][j] == 'O':
            my_map[i][j] = 3

bbang = 0
for time in range(N):
    if time == 0:
        minus_time()
        continue
    boom = minus_time()
    while boom:
        r, c = boom.pop()
        for dir in (1,0), (0,1), (-1,0), (0,-1):
            nr = r + dir[0]
            nc = c + dir[1]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            my_map[nr][nc] = 0
            bbang = 1
    if time % 2 == 1:
        fill_bomb()

# 최종 출력
for i in range(R):
    for j in range(C):
        if my_map[i][j] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print()
