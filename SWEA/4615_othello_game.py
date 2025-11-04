"""
SWEA_4615 - 재미있는 오셀로 게임 - D3

문제
- 오셀로라는 게임은 흑돌과 백돌을 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.
- 보드는 4x4, 6x6, 8x8 크기를 사용한다.
- 플레이어는 빈 공간에 돌을 놓을 수 있다.
- 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고,
- 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
"""

def check_stone(r, c, me):
    check = False
    dr = [-1, 0, 1, 0, -1, 1, 1, -1]
    dc = [0, 1, 0, -1, 1, 1, -1, -1]

    if me == 1:
        you = 2
    else:
        you = 1

    for dir in range(8):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if board[nr][nc] == you:    # 다음이 상대 돌이고
            new_r = nr + dr[dir]
            new_c = nc + dc[dir]
            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:  # 다다음이 내 돌인 경우
                continue
            if board[nr + dr[dir]][nc + dc[dir]] == me: # 나 - 너 - 나 인경우
                board[nr][nc] = me  # 바꾸기
                check = True
    if check:
        board[r][c] = me

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]

    half = N // 2
    board[half-1][half-1] = 2
    board[half-1][half] = 1
    board[half][half-1] = 1
    board[half][half] = 2

    for i in range(M):
        a, b, color = map(int, input().split())

        check_stone(b-1, a-1, color)
    
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{case+1} {black} {white}')