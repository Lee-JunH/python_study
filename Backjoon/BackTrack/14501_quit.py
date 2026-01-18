"""
Backjoon_14501 - 퇴사 - S3

문제
- 오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
- 최대한 많은 상담을 잡으라고 부탁을 했고, 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
- 각각의 상담을 완료하는데 걸리는 기간 T와 상담을 했을 때 받을 수 있는 금액 P로 이러우져 있다.
- 상담을 적절히 했을 때, 얻을 수 있는 최대 수익을 구하시오.
"""

def select_counsel(idx, time, price):
    global total_price

    if idx == N:
        if time != 0:
            return
        total_price = max(total_price, price)
        return
    
    if time:
        select_counsel(idx+1, time-1, price)
    else:
        select_counsel(idx+1, counsel[idx][0]-1, price + counsel[idx][1])
        select_counsel(idx+1, 0, price)

N = int(input())
counsel = [tuple(map(int, input().split())) for _ in range(N)]

cur_time = 0
total_price = 0

select_counsel(0, 0, 0)

print(total_price)