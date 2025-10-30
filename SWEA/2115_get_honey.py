"""
SWEA_2115 - 벌꿀채취 - 모의 SW 역량테스트

문제
- 각 벌통에 있는 꿀의 양이 주어졌을 때, 벌꿀을 채취하여 최대한 많은 수익을 얻으려고 한다.
- 2명의 일꾼이 있다. 꿀을 채취할 수 있는 벌통의 수는 M이고 가로로 연속하도록 선택한다.
- 2명의 일꾼이 선택한 벌통은 서로 겹치면 안된다.

풀이
- 모든 점에 대해서 좌표 2개를 받아와서 시작하기
- 시작 좌표로부터 M칸의 값의 합이 C보다 작은지 확인하기
- 두 좌표의 합을 구하고 max로 저장해놓기
"""

def double_value(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i] ** 2
    return result

def except_case(lst):
    # C보다 작은 조합 구하기
    big = 1
    result = 0
    for i in range(1<<M):
        my_lst = []
        for j in range(M):
            if i & (1<<j):
                my_lst.append(lst[j])
        hap = sum(my_lst)
        if hap <= C and hap >= big:
            big = hap
            temp = double_value(my_lst) # 합이 같아도 제곱이 작을 수 있으니까 처리
            if temp > result:
                result = temp
    return result

def find_max(pick):
    r, c = pick
    tong = []
    profit = 0

    for new_c in range(c, c+M):
        tong.append(honey[r][new_c])

    if sum(tong) <= C:
        profit = double_value(tong)
    else:
        profit = except_case(tong)

    return profit
    
T = int(input())
for case in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0
    first_big = 0
    for i in range(N):
        for j in range(N - M + 1):
            pick1 = (i, j)
            first_max = find_max(pick1)     # 첫번째 값 정하기
            if first_max < first_big:
                continue
            else:
                first_big = first_max

            second_big = 0
            for a in range(i, N):
                for b in range(N- M + 1):
                    if i == a:
                        b += j + M
                        if b >= N-M+1:
                            break
                    pick2 = (a, b)
                    second_max = find_max(pick2)    # 두번째 값 정하기
                    if second_max < second_big:
                        continue
                    else:
                        second_big = second_max
                    
                    if max_profit < first_max + second_max:
                        max_profit = first_max + second_max
    print(f'#{case+1} {max_profit}')