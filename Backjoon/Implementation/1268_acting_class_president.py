"""
Backjoon_1268 - 임시 반장 정하기 - S5

문제
- 자기 반 학생 중에서 1학년부터 5학년까지 지내오면서 같은 반이었던 사람이 가장 많은 학생이 임시반장이다.

풀이
- 각 학생들의 학년별 친구들을 set으로 저장해서 개수를 이용해 출력
"""

N = int(input())
my_class = [list(map(int, input().split())) for _ in range(N)]

student = [set() for _ in range(N)]

for grade in range(5):
    for a in range(N-1):  # a번 학생과
        for b in range(a+1, N):  # b번 학생 비교
            if my_class[a][grade] == my_class[b][grade]:    # a의 반 번호랑 b의 반 번호가 같으면
                student[a].add(b)   # a의 친구 리스트에 b추가
                student[b].add(a)   # b의 친구 리스트에 a추가

many_friend_student = 0 # 친구가 많은 학생의 번호
max_friend = -1         # 친구 수
for i in range(N):
    cur_friend = len(student[i])
    if cur_friend > max_friend:     # 친구 수가 많으면
        max_friend = cur_friend
        many_friend_student = i   # 학생번호 업데이트
print(many_friend_student)