# baekjoon_2628 - 종이자르기 - S5

garo, sero = map(int, input().split())
num = int(input())

li_g = [0, garo]
li_s = [0, sero]

for _ in range(num):
    gs, line = map(int,input().split())
    temp = 0
    if gs == 0:     # 가로 저장
        li_s.append(line)
    elif gs == 1:   # 세로 저장
        li_g.append(line)

li_g.sort() # 정렬하기
li_s.sort()
res_g = 0
res_s = 0

for i in range(1, len(li_g)):   # 가장 긴 세로 구하기
    temp = li_g[i] - li_g[i - 1]
    res_g = max(res_g, temp)
for i in range(1, len(li_s)):   # 가장 긴 가로 구하기
    temp = li_s[i] - li_s[i - 1]
    res_s = max(res_s, temp)

print(res_g * res_s)