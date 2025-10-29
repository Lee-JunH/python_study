"""
Backjoon_10709 - 기상캐스터 - S5

문제
- 각 구역의 하늘에는 구름이 있을 수도, 없을 수도 있다. 모든 구름은 1분이 지날 때마다 1킬로미터씩 동쪽으로 이동한다.
- 각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 예측하는 문제
"""

H, W = map(int, input().split())
cloud = [list(input().strip()) for _ in range(H)]

result = [[-1 for _ in range(W)] for _ in range(H)]

for i in range(H):
    next = False    # 구름을 만났는지 확인
    for j in range(W):
        if cloud[i][j] == 'c':
            result[i][j] = 0
            next = True
        else:
            if next:
                result[i][j] = result[i][j-1] + 1

for i in range(H):
    print(*result[i])