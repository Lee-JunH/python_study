# baekjoon_2669 - 직사각형 네개의 합집합의 면적 구하기 - S5

"""

"""

result=[[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())

    for x in range(x1,x2):
        for y in range(y1,y2):
            result[x][y] = 1
answer = 0
for j in result:
    answer += sum(j)
print(answer)