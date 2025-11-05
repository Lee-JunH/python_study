"""
Backjoon_20207 - 달력 - G5

문제
- 수현이는 1~365일로 표시된 달력에 계획을 표시해놨다.
- 연속된 두 일자에 각각 일정이 1개 이상 있다면 이를 일정이 연속되었다고 표현한다.
- 연속된 모든 일정은 하나의 직사각형에 포함된다.
- 연속된 일정을 모두 감싸는 가장 작은 직사각형의 크기만큼 코팅지를 오린다.

- 일정은 시작날짜와 종료날짜를 포함한다.
- 시작일이 가장 앞선 일정부터 차례대로 채워진다.
- 시작일이 같을 경우 일정의 기간이 긴 것이 먼저 채워진다.
- 일정은 가능한 최 상단에 배치된다.
- 일정 하나의 세로의 길이는 1이다. 
- 하루의 폭은 1이다. 
"""

N = int(input())
cal = [0 for _ in range(366)]

coting = 0
for _ in range(N):
    S, E = map(int, input().split())

    for i in range(S, E+1):
        cal[i] += 1

start = 0
height = 0
for i in range(366):
    height = max(height, cal[i])
    if start == 0 and cal[i] != 0:
        start = i
    if cal[i] == 0:
        end = i
        coting += (end - start) * height
        height = 0
        start = 0
if start != 0:
    coting += (366 - start) * height
print(coting)