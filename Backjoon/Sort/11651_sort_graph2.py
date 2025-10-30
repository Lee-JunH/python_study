"""
Backjoon_11651 - 좌표 정렬하기2 - S5

문제
- 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 문제
"""

N = int(input())
lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append((y,x))

lst.sort()

for y, x in lst:
    print(x, y)