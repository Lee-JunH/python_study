# 창고 다각형 - s2

num = int(input())
lst = []
for i in range(num):
    x, y = map(int, input().split())
    lst.append([x,y])
lst.sort()
result = 0
i = 0
for l in lst:
    if l[1] > result:
        result = l[1]
        idx = i
    i += 1

max = lst[0][1]
for i in range(idx):
    if max < lst[i+1][1]:
        result += ((lst[i+1][0] - lst[i][0]) * max)
        max = lst[i+1][1]
    else:
        result += ((lst[i+1][0] - lst[i][0]) * max)
         
max = lst[num-1][1]
for i in range(num-1, idx, -1):
    if max < lst[i-1][1]:
        result += ((lst[i][0] - lst[i-1][0]) * max)
        max = lst[i-1][1]
    else:
        result += ((lst[i][0] - lst[i-1][0]) * max)

print(result)