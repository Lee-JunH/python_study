"""
Backjoon_11650 - 좌표 정렬하기 - S5

문제
- 2차원 평면 위의 점 N개가 주어진다.
- 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 문제
"""

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()
for i in range(N):
    print(*lst[i])