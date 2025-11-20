"""
Backjoon_1022 - 소용돌이 예쁘게 출력하기 - G3

문제
- 크기가 무한인 정사각형 모눈종이가 있다.
- 모눈종이 전체를 양의 정수의 소용돌이 모양으로 채울 것이다.
- 일단 숫자 1을 0행 0열에 쓴다. 거기서 부터 반시계방향으로 시작된다.
- r1, c1, r2, c2가 입력으로 주어진다. 가장 왼쪽위, 가장 오른쪽 아래 칸.
    - 출력은 r1행부터 r2행까지 차례대로 출력
    - 공백의 길이는 최소
    - 모든 숫자의 길이는 같아야 한다.
    - 만약 수의 길이가 가장 길이가 긴 수보다 작다면, 왼쪽에서부터 공백을 삽입
범위 (-5,000 ≤ r1, c1, r2, c2 ≤ 5,000)

풀이
- 찾은 규칙
    - 0, 1, 2 일때 최대 값은 1, 9, 25, 49... 으로 1, 3, 5, 7,... 의 제곱 값이다.

"""

def num_len(num):
    length = 0
    if num == 0:
        return 1
    while num > 0:
        length += 1
        num //= 10
    return length

r1, c1, r2, c2 = map(int, input().split())

result = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

for r in range(r1, r2+1):
    for c in range(c1, c2+1):
        level = max(abs(r), abs(c))
        if level == 0:
            result[r-r1][c-c1] = 1
            continue

        one_line = (level + 1) * 2 - 1  # 한 변의 개수

        max_down = one_line ** 2
        max_left = max_down - one_line + 1
        max_up = max_left - one_line + 1
        max_right = max_up - one_line + 1

        if r == level:
            result[r-r1][c-c1] = max_down - (level-c)
        elif c == -level:
            result[r-r1][c-c1] = max_left - (level-r)
        elif r == -level:
            result[r-r1][c-c1] = max_up - (level+c)
        elif c == level:
            result[r-r1][c-c1] = max_right - (level+r)
max_num = 0
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        if result[i][j] > max_num:
            max_num = result[i][j]

max_len = num_len(max_num)   # 가장 긴 길이 찾기

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(f"{' ' * (max_len - num_len(result[i][j]))}{result[i][j]}", end=' ')
    print()