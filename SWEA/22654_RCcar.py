"""
SWEA_22654 - 차윤이의 RC카 - D2

문제
- NxN 필드가 주어진다.
    - 'G' : RC카가 이동 가능한 땅
    - 'T' : RC카가 이동이 불가능한 나무
    - 'X' : 현재 RC카의 위치
    - 'Y' : RC카를 이동 시키고자 하는 위치
- 조종기가 주어진다.
    - 'A' : 앞으로 이동
    - 'L' : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
    - 'R' : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전
- 처음 시작 방향은 위

- 목적지에 도달 할 수 있는지 확인하는 문제
"""

def find_position(pos):
    for i in range(N):
        for j in range(N):
            if field[i][j] == pos:
                return (i,j)

def move(a, b, d):
    if d == 0:      #up
        if a - 1 >= 0 and field[a-1][b] != 'T':
            return (a-1, b)
    elif d == 1:    #right
        if b + 1 < N and field[a][b+1] != 'T':
            return (a, b+1)
    elif d == 2:    #down
        if a + 1 < N and field[a+1][b] != 'T':
            return (a+1, b)
    elif d == 3:    #left
        if b - 1 >= 0 and field[a][b-1] != 'T':
            return (a, b-1)
    return (a, b)

T = int(input())
for case in range(T):
    N = int(input())
    field = [list(input().strip()) for _ in range(N)]
    Q = int(input())

    start_r, start_c = find_position('X')   # 출발 지점
    end_r, end_c = find_position('Y')       # 도착 지점
    # 방향은 위, 오른쪽, 아래, 왼쪽 순으로 0, 1, 2, 3 으로 설정

    print(f'#{case+1}', end=' ')
    for k in range(Q):
        C ,command = map(str, input().split())

        r = start_r
        c = start_c
        dir = 0
        for i in range(int(C)):
            if command[i] == 'A':   # 무빙
                r, c = move(r, c, dir)
            elif command[i] == 'L': # 방향 왼쪽으로
                if dir == 0:
                    dir = 3
                else:
                    dir = (dir - 1) % 4
            elif command[i] == 'R': # 방향 오른쪽으로
                dir = (dir + 1) % 4
        if r == end_r and c == end_c:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()