"""
Backjoon_2304 - 창고 다각형 - S1

문제
- N개의 높이가 다른 막대 기둥이 일렬로 세워져 있다. 이 창고의 지붕을 다음과 같이 만든다.
    - 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
    - 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
    - 지붕의 가장자리는 땅에 닿아야 한다.
    - 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
- 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.
"""

N = int(input())
warehouse = []

for _ in range(N):
    garo, sero = map(int, input().split())
    warehouse.append((garo, sero))

warehouse.sort()

max_h = 0
max_idx = 0
for i in range(N):    # 가장 높은 막대의 위치와 높이 찾기
    if warehouse[i][1] > max_h:
        max_h = warehouse[i][1]
        max_idx = i

result = max_h
max_h = warehouse[0][1]
for i in range(max_idx):    # 가장 높은 막대 전까지
    result += (warehouse[i+1][0] - warehouse[i][0]) * max_h
    if max_h < warehouse[i+1][1]:
        max_h = warehouse[i+1][1]

max_h = warehouse[-1][1]
for i in range(N-1, max_idx, -1):     # 거꾸로 확인
    result += (warehouse[i][0] - warehouse[i-1][0]) * max_h
    if max_h < warehouse[i-1][1]:
        max_h = warehouse[i-1][1]

print(result)