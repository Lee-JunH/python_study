"""
baekjoon_2669 - 직사각형 네개의 합집합의 면적 구하기 - S5

문제
- 4개의 직사각형이 놓여 있는데 밑변은 모두 가로축에 평행하다.
- 이 직사각형들이 차지하는 면적을 구하는 문제
"""

result = [[0 for _ in range(101)] for _ in range(101)]    #최대 범위로 만들기

answer = 0
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            if result[x][y] == 0:
                answer += 1
            result[x][y] = 1

print(answer)