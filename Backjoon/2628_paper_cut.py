# baekjoon_2628 - 종이자르기 - S5

g, s = map(int, input().split())
n = int(input())

garo = [0, g]
sero = [0, s]

for _ in range(n):
    op, cut = map(int, input().split())
    if op == 0:
        sero.append(cut)
    else:
        garo.append(cut)
garo.sort()
sero.sort()

r1 = 0
r2 = 0
for i in range(1, len(garo)):   # 가장 긴 세로 구하기
    r1 = max(r1, garo[i] - garo[i - 1])
for i in range(1, len(sero)):   # 가장 긴 가로 구하기
    r2 = max(r2, sero[i] - sero[i - 1])
print(r1 * r2)


# version 1
# garo, sero = map(int, input().split())
# num = int(input())

# li_g = [0, garo]
# li_s = [0, sero]

# for _ in range(num):
#     gs, line = map(int,input().split())
#     temp = 0
#     if gs == 0:     # 가로 저장
#         li_s.append(line)
#     elif gs == 1:   # 세로 저장
#         li_g.append(line)

# li_g.sort() # 정렬하기
# li_s.sort()
# res_g = 0
# res_s = 0

# for i in range(1, len(li_g)):   # 가장 긴 세로 구하기
#     temp = li_g[i] - li_g[i - 1]
#     res_g = max(res_g, temp)
# for i in range(1, len(li_s)):   # 가장 긴 가로 구하기
#     temp = li_s[i] - li_s[i - 1]
#     res_s = max(res_s, temp)

# print(res_g * res_s)