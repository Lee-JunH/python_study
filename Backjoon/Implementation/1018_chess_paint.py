"""
Backjoon_1018 - 체스판 다시 칠하기 - S3

문제
- 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
- 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
- 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우 2가지가 있다.
- 8x8 크기로 잘랐을 때 칠할 정사각형의 최소 개수 구하는 문제
"""

def check(r, c):
    count = 0
    count2 = 0
    for i in range(r, r+8):
        for j in range(c, c+8):
            if (i+j-r-c) % 2 == 0 and board[i][j] == 'W':
                count += 1
            elif (i+j-r-c) % 2 == 1 and board[i][j] == 'B':
                count += 1
            
            if (i+j-r-c) % 2 == 0 and board[i][j] == 'B':
                count2 += 1
            elif (i+j-r-c) % 2 == 1 and board[i][j] == 'W':
                count2 += 1
    return count, count2

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

min_count = float('inf')
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        a, b = check(i,j)
        min_count = min(a, b, min_count)

print(min_count)