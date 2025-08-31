"""
backjoon_17136 - 색종이 붙이기 - G2

문제
- 정사각형 모양 1~5 크기의 색종이 5장씩 가지고 있다.
- 10x10인 종이 위에 1이 적힌 칸은 모두 색종이로 붙이려고 한다.
- 종이를 붙일 때
    - 종이의 경계 밖으로 나가서는 안되고
    - 겹쳐도 안되고
    - 칸의 경계와 일치하게 붙여야 한다.
    - 0이 적힌 칸에는 색종이가 있으면 안된다.

출력
- 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수

풀이
- 파리 퇴치와 비슷하게 색종이로 덮을 수 있는 정사각형을 찾는다.
- 큰 색종이부터 탐색하자.
- 근데 6x6 이상인 경우는 큰것 부터 채우는 것보다 작은 경우의 수가 존재한다.
    - 그러면 하드코딩으로 개수를 정하고 시작할까?
    - 짝수인 경우는 예외로 6인 경우 3x3 4개, 8 - 4개, 10 - 4개
"""

def find_one(r, c):     # r,c 다음 칸들 중 1인 인덱스 찾기
    temp = r
    for i in range(r, N):
        if i > temp:
            c = 0
        for j in range(c, N):
            if paper[i][j] == 1:
                return i, j
    return 10, 0 # 없으면 마지막으로
    

def square(r, c, size): # size로 덮이는지 확인
    hap = 0
    if r+size > 10 or c+size > 10:
        return 0
    for i in range(r, r+size):
        for j in range(c, c+size):
            hap += paper[i][j]
    if hap == size**2:
        return 1
    return 0

def draw_paper(r, c, size, num):    # 색칠하기
    for i in range(r, r+size):
        for j in range(c, c+size):
            paper[i][j] = num

def backtrack(r, c):
    global min_cnt

    r, c = find_one(r, c)   # 1인 지점 찾아서 시작하기

    if r == 10 and c == 0:   # 마지막까지 봤을 때 개수 확인
        if sum(color) < min_cnt:   # 개수가 min값이면 업데이트
            min_cnt = sum(color)
        return
    
    for i in range(5, 0, -1):   # 색종이 채우기
        if color[i] == 5:   # 색종이가 이미 5장이면 다음 색종이
            continue

        if square(r, c, i): # 채울 수 있는지 보고
            color[i] += 1   # 덮이는 색 +1
            draw_paper(r, c, i, 0)  # 0으로 덮기

            backtrack(r, c)
            
            # 돌아와서 다른 색종이로 채워보기 위해 다시 채우기
            draw_paper(r, c, i, 1)
            color[i] -= 1
            # 다음 크기의 색종이로 채우기

N = 10
paper = [list(map(int, input().split())) for _ in range(N)]

# 각 종이 개수 변수
color = [0 for _ in range(6)]   # 사용한 색종이 리스트

min_cnt = 26
backtrack(0, 0)    # 시작하는 위치(0,0), 색종이 사용 횟수

if min_cnt == 26:
    print(-1)
else:
    print(min_cnt)