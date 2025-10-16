"""
Backjoon_13220 - Secret - G5

문제
- 비밀번호는 N개의 공백으로 구분된 정수로 이루어져 있다.
- 비밀번호가 "37 20 71 33 97"이면 앨리스는 비밀번호를 "20 71 33 97 37"로 적는다.
- 두 루프가 주어질 때 같은 비밀번호인지 확인하는 문제

풀이
- 전에 배웠던 KMP 알고리즘 사용하기
    - 근데 모른다...
- 다른 방법을 생각해보자
- 무조건 a를 베이스 문자열이라고 생각하면
- a+a 안에 b가 있으면 된다.?
-대박대박
"""

N = int(input())
a = list(input().split())
b = list(input().split())

a.extend(a)

a_string = ' '.join(a)
b_string = ' '.join(b)

if b_string in a_string:
    print('YES')
else:
    print('NO')