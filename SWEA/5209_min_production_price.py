"""
SWEA_5209 - 최소 생산 비용 - D3

문제
- 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.
- 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 문제
"""

# 공장번호, 현재까지 가격
def backtrack(num, price):
    global min_price

    if price > min_price:   # 이미 넘어가면 종료
        return
    
    if num == N:
        min_price = min(min_price, price)   # 마지막까지 왔으면 업데이트 후 종료
        return
    
    for i in range(N):
        if not factory[i]:  # 아직 생산안한 공장이면
            factory[i] = 1
            backtrack(num+1, price + V[num][i])     # 가격에 추가하여 백트래킹
            factory[i] = 0

T = int(input())
for case in range(T):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    min_price = 99 * 15     # 최대 비용 99에 15개의 공장
    factory = [0] * N

    backtrack(0, 0)

    print(f'#{case+1} {min_price}')