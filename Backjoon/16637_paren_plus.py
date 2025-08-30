"""
backjoon_16637 - 괄호 추가 - G3

문제
- 0~9의 정수와 '+-x'의 연산자로 이루어진  길이 N의 수식이 있다.
- 연산자 우선순위는 모두 동일하다.
- 수식에 괄호를 추가하면, 괄호 안 식을 먼저 계산해야 한다
- 중첩된 괄호는 사용할 수 없다
- 괄호를 적절히 추가해 만들 수 있는 식의 결과 최댓값을 구하라

풀이
- 어케풀라는거야~~~~
- 괄호를 넣을 수 있는 자리를 찾아보자
- 처음에는 안넣은 것과 같으니까 넘어간다
- 
"""

def check_sik():
    my_stack.append('(')
    

N = int(input())
sik = list(input().strip())

my_stack = [sik[0]]
for i in range(1, N):
    if sik[i] in '+-*':
        my_stack.append(sik[i])
        check_sik()