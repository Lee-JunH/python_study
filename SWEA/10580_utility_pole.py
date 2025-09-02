"""
SWEA_10580 - 전봇대 - D3

문제
- 전선들이 복잡하게 꼬여 있는 전봇대 2개가 있다.
- 두 전봇대는 높이가 매우 높고, N개의 팽팽한 전선으로 연결되어 있다.
- 두 전선이 끝점이 같은 경우는 없으나 교차하는 경우는 있다.
- 3개 이상의 전선이 하나의 점에서 만나지 않을 때 전봇대의 교차점의 개수는?

풀이
- 막대를 그었을 때 작은 곳에서 큰 값으로 갈 때
    - [0]보다 작고 [1]보다 큰게 있으면 + 1
- 큰 곳에서 작은 값으로 갈 때
    - s ~ end 사이에 끝 점이 있으면
"""

T = int(input())
for case in range(T):
    N = int(input())
    pole = [list(map(int, input().split())) for _ in range(N)]

    board = [0 for _ in range(10000)]

    cnt = 0
    for i in range(N):
        p1 = pole[i]
        for j in range(i+1, N):
            p2 = pole[j]
            if p1[0] < p1[1]:
                if p1[0] < p2[0] and p1[1] < p2[1]:
                    pass
                elif p1[0] > p2[0] and p1[1] > p2[1]:
                    pass
                else:
                    cnt += 1
            else:
                if p1[0] < p2[0] and p1[1] < p2[1]:
                    pass
                elif p1[0] > p2[0] and p1[1] > p2[1]:
                    pass
                else:
                    cnt += 1

    print(f'#{case+1} {cnt}')