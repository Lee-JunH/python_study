"""
Backnoon_14658 - 하늘에서 별똥별이 빗발친다 - G3

문제
- 네모난 L*L 크기의 트램펄린이 있다. 별똥별이 어디로 떨어질지는 이미 알고 있기 때문에
- 트램펄린으로 최대한 많은 별똥별을 튕겨낼 계획이다.
- 최대한 많은 별똥별을 튕겨내도록 배치했을 때, 지구에는 몇 개의 별똥별이 부딪히게 될까?
- (별똥별이 떨어지는 위치는 겹치지 않고 트램펄린의 모서리에 부딪혀도 튕겨나간다.)
- 트램펄린은 비스듬하게 배치할 수 없다.

풀이
- 별똥별 한 점을 트램펄린의 왼쪽 아래 꼭지점으로 생각한다.
- 추가로 트램펄린의 왼쪽 위 꼭지점으로도 생각해야 한다.
- x좌표 구간과 y좌표 구간을 같이 확인해야 한다.
"""

# N: 별똥별이 떨어지는 구역의 가로길이, M: 세로길이, L: 트램펄린 한변의 길이, K: 별똥별의 개수
N, M, L, K = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(K)]

max_stars = 0

for i in range(K):
    for j in range(K):
        nx = stars[i][0]
        ny = stars[j][1]
        
        star = 0
        for k in range(K):
            sx, sy = stars[k]
            if nx <= sx <= nx + L and ny <= sy <= ny + L:
                star += 1
        max_stars = max(max_stars, star)

print(K - max_stars)


# N, M, L, K = map(int, input().split())

# stars = [tuple(map(int, input().split())) for _ in range(K)]

# max_stars = 0
# for x, y in stars:
#     star1 = 0
#     for nx, ny in stars:    # 왼쪽 아래
#         if x <= nx <= x + L and y - L <= ny <= y:
#             star1 += 1
#     star2 = 0
#     for nx, ny in stars:    # 왼쪽 위
#         if x <= nx <= x + L and y <= ny <= y + L:
#             star2 += 1
#     star3 = 0
#     for nx, ny in stars:    # 오른쪽 위
#         if x - L <= nx <= x and y <= ny <= y + L:
#             star3 += 1
#     star4 = 0
#     for nx, ny in stars:    # 오른쪽 아래
#         if x - L <= nx <= x and y - L <= ny <= y:
#             star4 += 1
#     max_stars = max(max_stars, star1, star2, star3, star4)
# print(K - max_stars)