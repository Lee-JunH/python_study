"""
SWEA_20551 - 증가하는 사탕 수열 - D3

문제
- 각 상자마다 사탕이 A, B, C개 들어있다.
- 각 상자에 들어 있는 사탕의 개수가 순 증가하기 위해 먹어야할 사탕의 최소 개수를 구하는 문제

풀이
- 맨 뒤값을 기준으로 앞의 값과 비교하여 해결한다.
"""

def my_candy():
    muk = 0
    check2 = 0

    max2 = C - 1
    if max2 <= 1:
        return -1
    
    if B > max2:
        muk += B - max2
        check2 = 1
    
    if check2:  # 변경한 경우
        max1 = max2 - 1
    else:   # 변경 안한 경우
        max1 = B - 1
        if max1 == 0:
            return -1

    if A > max1:
        muk += A - max1

    return muk

T = int(input())
for case in range(T):
    A, B, C = map(int, input().split())
    
    print(f'#{case+1} {my_candy()}')