"""
Backjoon_13300 - 방 배정 - B2

문제
- 1학년부터 6학년까지 묵을 방을 정해야 한다.
- 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다.
- 한 방에는 같은 학년의 학생들을 배정해야한다.
- 한 방에 한 명만 배정하는 것도 가능하다.
- 한 방에 최대 K명일 때 모든 학생을 배정하기 위해 필요한 방의 최소 개수는?
"""

N, K = map(int, input().split())

room = 0
grade_girl = [0 for _ in range(7)]
grade_boy = [0 for _ in range(7)]
for _ in range(N):
    S, Y = map(int, input().split())
    
    if S == 1:  # 남자인 경우
        grade_boy[Y] += 1
    else:       # 여자인 경우
        grade_girl[Y] += 1

for i in range(1, 7):
    if grade_girl[i] % K == 0:
        room += grade_girl[i] // K
    else:
        room += grade_girl[i] // K + 1
    if grade_boy[i] % K == 0:
        room += grade_boy[i] // K
    else:
        room += grade_boy[i] // K + 1
print(room)