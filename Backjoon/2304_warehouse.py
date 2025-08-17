# baekjoon_2304 - 창고 다각형 - S2

num = int(input())
lst = []
for i in range(num):
    x, y = map(int, input().split())
    lst.append([x,y])
lst.sort()
result = 0
i = 0
for x, y in lst:    # 가장 높은 막대의 위치와 높이 찾기
    if y > result:
        result = y
        idx = i
    i += 1

max = lst[0][1]
for i in range(idx):    # 가장 높은 막대 전까지
    if max < lst[i+1][1]:   # 더 높은 막대 만나면
        result += ((lst[i+1][0] - lst[i][0]) * max)
        max = lst[i+1][1]
    else:
        result += ((lst[i+1][0] - lst[i][0]) * max)
         
max = lst[num-1][1]     # 거꾸로 확인
for i in range(num-1, idx, -1):
    if max < lst[i-1][1]:
        result += ((lst[i][0] - lst[i-1][0]) * max)
        max = lst[i-1][1]
    else:
        result += ((lst[i][0] - lst[i-1][0]) * max)

print(result)