"""
Backjoon_16235 - 나무 재테크 - G3

문제
- 부동산 투자로 억대의 돈을 번 상도는 부럽다.
- 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
- 같은 1x1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
- 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
    - 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
    - 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
- 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
    - 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
- 가을에는 나무가 번식한다. 
    - 번식하는 나무는 나이가 5의 배수이어야 하며
    - 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
- 겨울에는 로봇 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
    - 각 칸에 추가되는 양분의 양은 A[r][c]이다.
- K년이 지난 후 상도의 땅에 살아있는 나무의 개수는?
"""

def spring():
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for k in range(len(trees[i][j])):
                    if food[i][j] >= trees[i][j][k]:
                        food[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                    else:
                        for _ in range(k, len(trees[i][j])):
                            food[i][j] += trees[i][j].pop() // 2
                        break
    return

def summer():
    pass

def autumn():
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)
            food[i][j] += dead[i][j]
    return

def winter():
    pass

N, M, K = map(int, input().split())     # N: 쿠기, M: 심는 나무, K: 지난 년 수
A = [list(map(int, input().split())) for _ in range(N)]
tree_temp = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
food = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
dead = [[0 for _ in range(N)] for _ in range(N)]

for x, y, z in tree_temp:        # 나무 정보 입력
    trees[x-1][y-1].append(z)

for _ in range(K):
    spring()
    summer()
    autumn()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])
print(answer)