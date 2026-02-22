"""
Backjoon_5014 - 스타트링크 - S1

문제
- 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 스타트링크가 있는 곳의 위치는 G층이다.
- 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.
- 엘리베이터에는 U버튼(U층을 가는 버튼), D버튼 (아래로 D층을 가는 버튼)이 있다.
- (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)
- G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성하라.
- 갈 수 없다면, "use the stairs"를 출력
"""

def bfs():  
    my_q = [S]

    check[S] = 1

    while my_q:
        cur = my_q.pop()

        if cur == G:
            return check[cur] - 1
        else:
            for next in (cur + U, cur - D):
                if (0 < next <= F) and check[next] == 0:
                    check[next] = check[cur] + 1
                    my_q.append(next)

    return "use the stairs"

F, S, G, U, D = map(int, input().split())

check = [0 for _ in range(F + 1)]

print(bfs())