"""
Backjoon_14626 - ISBN - B1

문제
- ISBN(International Standard Book Number)은 전 세계 모든 도서에 부여된 고유번호로, 국제 표준 도서번호이다.
- 13자리의 숫자로 마지막 숫자는 체크기호로 정확성 여부를 점검하는 숫자이다.
- 이 체크기호는 일련번호의 앞에서부터 각 자리마다 가중치를 곱한 것을 모두 더하고, 그 값을 10으로 나눈 나머지가 0이 되도록 만드는 숫자 m을 사용한다.
- 손상된 자리의 숫자를 찾아라.
"""

isbn = input()

num = 0

check = 1
for i in range(13):
    if i % 2 == 0:
        if isbn[i] == '*':
            check = 1
            continue
        num += int(isbn[i])
    else:
        if isbn[i] == '*':
            check = 3
            continue
        num += 3 * int(isbn[i])
if num % 10 == 0:
    new = 0
elif check == 1:
    new = 10 - num % 10
else:
    i = 1
    while True:
        if (num+(3*i)) % 10 == 0:
            new = i
            break
        i += 1
print(new)