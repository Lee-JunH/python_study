"""
Backjoon_15685 - 드래곤 커브 - G3

문제
- 드래곤 커브는 3가지 속성으로 이루어져 있다.
    - 시작 점
    - 시작 방향
    - 세대
- 0 세대 드래곤 커브는 길이가 1인 선분이다.
- 1 세대 드래곤 커브는 0세대 드래곤 커브를 끝 점을 기준으로
- 시계 방향으로 90도 회전시킨 다음 0세대 드래곤 커브의 끝 점에 붙인 것이다.
- 2 세대 드래곤 커브도 1세대를 만든 방법을 이용한다.
- 즉 K세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계방향 회전시킨 다음, 끝점에 붙인 것
- 드래곤 커브 N개가 있을 때 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수는?
- 0: 우, 1: 위, 2: 좌, 3: 아래
"""

def count_square():
    pass

def dragon_curve(gen):
    for i in range(gen):
        pass

N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())

    dragon_curve(g)

print(count_square())