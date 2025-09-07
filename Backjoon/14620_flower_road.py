"""
backjoon_14620 - 꽃길 - S2

문제
- 꽃의 씨앗은 꽃을 심고 1년 후에 꽃이 피므로 다음해 식목일부터 꽃길을 걸을 수 있다.
- 꽃의 씨앗이 3개밖에 없었으므로 3개의 꽃이 하나도 죽지 않고 1년후에 꽃잎이 만개하길 원한다.
- 어떤 씨앗이 꽃이 핀 뒤 다른 꽃잎과 닿게 될 경우 두 꽃 모두 죽는다.
- 화단 밖으로 나가도 죽는다.

출력
- 꽃을 정상적으로 폈을 때 가장 싼 가격에 화단을 대여하는 최소비용을 구하는 문제

풀이
- 구해야할 것
    1. 3개의 씨앗을 정상적으로 심는 위치
        - 정상적으로 피기 위해서 테두리는 심지 못함
        - 위, 아래, 오, 왼 은 1칸, 대각선 인 경우는 심지 못함
        - 위 2가지 경우를 제외하여 심어보고 최소인 합을 구한다.
    2. 그 위치에서의 화단 가격
        - 자기 위치를 포함하여 옆의 값들을 합한다.

- 아니면 화단 가격이 작은 것 3개를 배치가능한지를 확인하는 방법은 어떤가?

풀이시간
- 50분
"""

def ddang_price(r, c):  # 땅값 계산 함수
    result = 0
    for dir in range(5):
        result += price[r+dr[dir]][c+dc[dir]]
    return result

def flower(r, c, num):  # 방문 체크 및 해제 함수
    for dir in range(5):
        vis[r+dr[dir]][c+dc[dir]] = num

def check(r, c):    # 배치 가능한지 확인하는 함수
    for dir in range(1, 5):
        if vis[r+dr[dir]][c+dc[dir]] == 1:
            return 0
    return 1

def backtrack(hap, cnt):   # 꽃 배치 함수
    global min_price

    if cnt == 3:     # 3개 배치한 경우 업데이트 및 리턴
        min_price = min(min_price, hap)
        return
    
    if hap > min_price:     # 이미 큰경우 리턴
        return

    for i in range(1, N-1):
        for j in range(1, N-1):
            if not check(i,j):
                continue
            flower(i,j,1)
            ddang = ddang_price(i,j)
            backtrack(hap+ddang, cnt+1)
            flower(i,j,0)


N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

min_price = 3001    # 최대 가격 = (200*5) * 3개

vis = [[0 for _ in range(N)] for _ in range(N)]
backtrack(0, 0)

print(min_price)