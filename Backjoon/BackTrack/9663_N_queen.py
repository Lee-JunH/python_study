"""
Backjoon_9663 - N_Queen - G4

문제
- N-Queen 문제는 크기가 NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
- N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

풀이
- 퀸을 놓았을 때 가로, 세로, 대각선에 다른 퀸을 놓을 수 없다.
    - 대각선은 좌표값의 합 또는 차 값이 같은 구역을 모두 체크하면 된다.
- 백트래킹으로 놓으면서 안되는 경우 돌아가도록 하자.
"""

def n_queen(row):
    global cnt

    if row == N:
        cnt += 1
        return
    
    for col in range(N):
        if not sero[col] and not cross_up[row+col] and not cross_down[row + (N-1) - col]:
            sero[col] = 1
            cross_up[row+col] = 1
            cross_down[row-col + (N-1)] = 1
            n_queen(row+1)
            sero[col] = 0
            cross_up[row+col] = 0
            cross_down[row-col + (N-1)] = 0

N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

sero = [0] * N
cross_up = [0] * (2 * (N-1) + 1)
cross_down = [0] * (2 * (N-1) + 1)

cnt = 0

n_queen(0)

print(cnt)