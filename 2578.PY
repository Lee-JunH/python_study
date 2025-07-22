# 빙고 - s4

board = [list(map(int, input().split())) for _ in range(5)]

bingo = [list(map(int, input().split())) for _ in range(5)]

def find_num(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return i, j

count = 0
def find_line(lst):
    for i in range(5):
        if sum(lst[x][i] for x in range(5)) == 5:
            count += 1
        if sum(lst[i][x] for x in range(5)) == 5:
            count += 1
        if sum(lst[x][x] for x in range(5)) == 5:
            count += 1
        if sum(lst[x][4-x] for x in range(5)) == 5:
            count += 1
    return count

result = []
for i in range(5):
    for j in range(5):
        count += 1
        x, y = find_num(board, bingo[i][j])
        result[x][y] = 1
        count = find_line(result)
        if count >= 3:
            break
    if count >= 3:
        break
print(count)