"""
backjoon_7568 - 덩치 - S5

문제
- 어떤 사람의 몸무게가 x kg 이고 키가 y cm라면 이사람의 덩치는 (x, y)로 표시된다.
- 키와 몸무게 모두 큰경우 더 크다라고 말한다.
- 각 사람의 덩치 등수는 자신보다 더 큰 덩치의 사람 수로 정해진다.
- 같은 덩치 등수를 가진 사람은 여러명도 가능하다.

출력
- N명의 덩치 등수를 계산하여 출력

풀이
- 리스트로 저장하고 더 큰 덩치의 수를 센다.
"""

N = int(input())
dc = []
for _ in range(N):
    mom, h = map(int, input().split())
    dc.append((mom, h))

grade = [1 for _ in range(N)]   # 등수 저장 리스트
for i in range(N):
    for j in range(N):
        if j == i:
            continue
        if dc[i][0] < dc[j][0] and dc[i][1] < dc[j][1]: # 몸무게, 키 둘다 큰 경우
            grade[i] += 1
print(*grade)