"""
Backjoon_1268 - 임시 반장 정하기 - S5

문제
- 자기 반 학생 중에서 1학년부터 5학년까지 지내오면서 같은 반이었던 사람이 가장 많은 학생이 임시반장
"""

N = int(input())
my_class = [list(map(int, input().split())) for _ in range(N)]

student = [set() for _ in range(N)]

for grade in range(5):
    for a in range(N-1):  # a번 학생과
        for b in range(a+1, N):  # b번 학생 비교
            if my_class[a][grade] == my_class[b][grade]:    # a의 반 번호랑 b의 반 번호가 같으면
                student[a].add(b)
                student[b].add(a)

many_friend_student = 0
max_friend = -1
for i in range(N):
    cur_friend = len(student[i])
    if cur_friend > max_friend:
        max_friend = cur_friend
        many_friend_student = i+1
print(many_friend_student)