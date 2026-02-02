"""
Backjoon_21608 - 상어 초등학교 - G5

문제
- 교실은 NxN크기의 격자로 나타낼 수 있다. 학교에 다니는 학생의 수는 N^2명이다.
- 오늘은 모든 학생의 자리를 정하는 날이다.
- 선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다.
- 한 칸에는 학생 한 명의 자리만 있을 수 있고, |r1-r2| + |c1-c2| = 1을 만족하는 두칸이 (r1, c1), (r2, c2)를 인접한다.
    1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 정한다.
    2. 1이 여러 개인 경우, 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 정한다.
    3. 2가 여러 개인 경우, 행의 번호가 가장 작은칸으로 한다.
    4. 3이 여러 개인 경우, 열의 번호가 가장 작은 칸으로 한다.
- 학생의 만족도는 자리 배치가 끝난 후 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
- 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.

풀이
- |r1-r2| + |c1-c2| = 1의 뜻은 두 식 중 하나는 1 하나는 0이기 때문에 칸의 상하좌우를 뜻한다.
"""

N = int(input())
seats = [[0 for _ in range(N)] for _ in range(N)]
friends = [list(map(int, input().split())) for _ in range(N*N)]

for i in range(N*N):
    num = friends[i][0]
    friend = friends[i][1:]
    check = []
    
    for i in range(N):
        for j in range(N):
            if not seats[i][j]:
                empty = 0
                like = 0
                
                for dr, dc in (0,1), (1,0), (0,-1), (-1,0):
                    nr = i + dr
                    nc = j + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    if seats[nr][nc] == 0:
                        empty += 1
                    elif seats[nr][nc] in friend:
                        like += 1
                check.append([like, empty, i, j])
    check.sort(reverse=True)
    seats[check[0][2]][check[0][3]] = num

result = 0
satisfaction = [0, 1, 10, 100, 1000]

friends.sort()
for i in range(N):
    for j in range(N):
        cnt = 0

        for dr, dc in (0,1), (1,0), (0,-1), (-1,0):
            nr = i + dr
            nc = j + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if seats[nr][nc] in friends[seats[i][j] - 1]:
                cnt += 1

        result += satisfaction[cnt]

print(result)