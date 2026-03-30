"""
Backjoon_30804 - 과일 탕후루 - S2

문제
- 긴 막대에 N개의 과일이 꽂혀있는 과일 탕후루를 만들었다.
- 과일의 각 종류에는 1~9까지의 번호가 붙어있고, 앞쪽부터 차례로 S1,S2,... 과일이 꽂혀있다.
- 주문을 다시 확인해보니 과일을 두 종류 이하로 사용해달라는 요청이 있었다.
- 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했다.
- 앞에서 a개, 뒤에서 b개의 과일을 빼면 S(a+1), S(a+2),...S(N-b-1), 번 과일
  총 N - (a + b) 개가 꽂혀있는 탕후루가 된다.
- 이렇게 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하시오.

풀이
- 앞에서부터 확인해서 fruit에 과일종류를 계속 센다.
"""

N = int(input())
S = list(map(int, input().split()))

a = 0
b = 0 
fruit = {}
max_fruit = 0

while a < N:
    num = S[a]

    if num in fruit:
        fruit[num] += 1
    else:
        fruit[num] = 1
    
    while len(fruit) > 2:
        fruit[S[b]] -= 1
        if fruit[S[b]] == 0:
            del fruit[S[b]]     # 집합 삭제
        b += 1
    max_fruit = max(max_fruit, a - b + 1)
    a += 1

print(max_fruit)