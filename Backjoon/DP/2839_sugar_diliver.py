"""
backjoon_2839 - 설탕 배달 - S4

문제
- 설탕을 N kg 배달한다. 봉지는 3kg, 5kg 이 있다.
- 배달하는 봉지의 최소 개수를 구하라.

출력
- 정확하게 N kg을 만들 수 없다면 -1, 그 외는 봉지의 최소 개수

풀이
- 3*x + 5*y = N 인 식이다. 최소 개수이기 때문에 y 최대값부터 줄이면서 확인
"""

def sugar():
    y_max = N // 5
    x_max = N // 3
    for y in range(y_max, -1, -1):
        for x in range(0, x_max + 1):
            if 3*x + 5*y == N:
                return x+y
    return -1

N = int(input())
print(sugar())