"""
Backjoon_2477 - 참외밭 - S2

* 문제
- 참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90, 180, 270도 회전한 모양의 육각형이다.
- 1m^2의 넓이에 자라는 참외의 개수와
- 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는
- 변의 방향과 길이가 주어진다.
- 참외밭에서 자라는 참외의 수를 구하라.

* 입력
- 변의 방향에서 동쪽은 1, 서쪽 2, 남쪽 3, 북쪽 4

* 풀이
- 가장 긴곳과 붙어있는 두 값의 차이를 이용
"""

K = int(input())
order = []
my_lst = [list(map(int, input().split())) for _ in range(6)]

# 전체 넓이 구하기
garo = 0
garo_i = 0
sero = 0
sero_i = 0
for i in range(6):
    if my_lst[i][0] == 1 or my_lst[i][0] == 2:
        if garo < my_lst[i][1]:
            garo = my_lst[i][1]
            garo_i = i  # 가장 긴 가로의 인덱스 저장
    elif my_lst[i][0] == 3 or my_lst[i][0] == 4:
        if sero < my_lst[i][1]:
            sero = my_lst[i][1]
            sero_i = i  # 가장 긴 세로의 인덱스 저장
result = garo * sero

# 뺄 넓이 구하기
cut_sero = abs(my_lst[(garo_i+1) % 6][1] - my_lst[garo_i-1][1]) # 인덱스 초과 방지
cut_garo = abs(my_lst[(sero_i+1) % 6][1] - my_lst[sero_i-1][1]) # -는 어차피 끝값

result -= cut_garo * cut_sero

print(result * K)