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


중요한 조건
- 중첩이 안되기 때문에 괄호를 넣을 자리는 각 연산자 위치 이다.
- 즉 연속된 연산자에는 괄호를 넣지 못한다.
- 또한 처음에는 안넣은 것과 동일하다.
"""

def dfs_sik(index, cur):    # 괄호 계산을 할 인덱스, 현재 합
    global max_hap
    
    if index == len(sik):
        if max_value < cur:
            max_value = cur
        return

    next = cur, sik[index], sik[index-1]
    dfs_sik(index+2, next)

    if index+4 <= len(sik):
        temp = sik[index+1], sik[index+3], sik[index+2]
        next = cur, temp, sik[index]
        dfs(index+4, next)

N = int(input())
sik = list(input().strip())

max_hap = 0
dfs_sik(1, int(sik[0]))
print(max_hap)