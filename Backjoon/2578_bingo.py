# baekjoon_2578 - 빙고 - S4

board = [list(map(int, input().split())) for _ in range(5)]

bingo = [list(map(int, input().split())) for _ in range(5)]

def find_num(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return i, j

def find_line(lst):
    count = 0
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

lst = [[0] * 5 for x in range(5)]
count_sah = 0
count = 0
for i in range(5):
    for j in range(5):
        count_sah += 1
        x, y = find_num(board, bingo[i][j])
        lst[x][y] = 1
        count = find_line(lst)
        if count >= 3:
            break
    if count >= 3:
        break
print(count_sah)