"""
Backjoon_2529 - 부등호 - S1

문제
- 두 종류의 부등호 기호 '<'와 '>'가 k개 나열된 순서열 A가 있다.
- 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다.
- 부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 선택된 숫자는 모두 달라야 한다.
- 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다.
"""

def check_sign(n, new_num, new_sign):
    if new_sign == '>':
        return n > new_num
    if new_sign == '<':
        return n < new_num

def dfs(num, cnt):
    global max_num, min_num

    if cnt == k+1:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    
    for i in range(10):
        if vis[i]:
            continue
        if cnt == 0 or check_sign(num%10, i, sign[cnt-1]):
            vis[i] = 1
            dfs(num*10 + i, cnt+1)
            vis[i] = 0

k = int(input())
sign = list(input().split())

max_num = 0
min_num = 9876543210

vis = [0 for _ in range(10)]
dfs(0, 0)

if len(str(max_num)) == k:
    print(0, end='')
    print(max_num)
else:
    print(max_num)

if len(str(min_num)) == k:
    print(0, end='')
    print(min_num)
else:
    print(min_num)