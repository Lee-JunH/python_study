# 종이자르기 - s5

garo, sero = map(int, input().split())
num = int(input())
li_g = [0]
li_s = [0]
for _ in range(num):
    gs, line = map(int,input().split())
    temp = 0
    if gs == 0:
        li_s.append(line)
    elif gs == 1:
        li_g.append(line)
li_g.append(garo)
li_s.append(sero)
res_g = 0
res_s = 0
li_g.sort()
li_s.sort()
for i in range(1, len(li_g)):
    temp = li_g[i] - li_g[i - 1]
    res_g = max(res_g, temp)
for i in range(1, len(li_s)):
    temp = li_s[i] - li_s[i - 1]
    res_s = max(res_s, temp)

print(res_g * res_s)