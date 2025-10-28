"""
Backjoon_10814 - 나이순 정렬 - S5

문제
- 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 문제
"""

N = int(input())

customer = []
for i in range(N):
    age, name = input().split()
    customer.append((int(age), i, name))

customer.sort()

for i in range(N):
    age, _, name = customer[i]
    print(f'{age} {name}')