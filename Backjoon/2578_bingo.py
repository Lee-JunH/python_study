# baekjoon_2578 - 빙고 - S4


def find_num(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return i, j

def find_line(lst):
    count = 0
    for i in range(5):
        if sum(lst[x][i] for x in range(5)) == 5:  # 세로 check
            count += 1
        if sum(lst[i][x] for x in range(5)) == 5:  # 가로 check
            count += 1
    if sum(lst[x][x] for x in range(5)) == 5:   # 오른쪽 아래 라인 check
        count += 1
    if sum(lst[x][4-x] for x in range(5)) == 5: # 오른쪽 위 라인 cheeck
        count += 1
    return count


board = [list(map(int, input().split())) for _ in range(5)] # 빙고판 입력
bingo = [list(map(int, input().split())) for _ in range(5)] # 사회자 숫자 입력

lst = [[0] * 5 for x in range(5)]   # 체크할 리스트
count_sah = 0   # 사회자가 부른 숫자 개수
count = 0
for i in range(5):
    for j in range(5):
        count_sah += 1
        x, y = find_num(board, bingo[i][j]) # 빙고판에서 부른 숫자 위치 찾기
        lst[x][y] = 1
        count = find_line(lst)  # 라인 개수 세기
        if count >= 3:  # 빙고면 break
            break
    if count >= 3:
        break
print(count_sah)