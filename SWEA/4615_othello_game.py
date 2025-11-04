"""
SWEA_4615 - 재미있는 오셀로 게임 - D3

문제
- 오셀로라는 게임은 흑돌과 백돌을 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.
- 보드는 4x4, 6x6, 8x8 크기를 사용한다.
- 플레이어는 빈 공간에 돌을 놓을 수 있다.
- 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고,
- 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
"""

def check():
    black = []
    white = []
    

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]

    half = N // 2
    board[half-1][half-1] = 'W'
    board[half-1][half] = 'B'
    board[half][half-1] = 'B'
    board[half][half] = 'W'

    for i in range(M):
        a, b, color = map(int, input().split())
        if color == 1:
            pass
        elif color == 0:
            pass
    