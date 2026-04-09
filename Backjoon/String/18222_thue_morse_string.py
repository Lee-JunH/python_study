"""
Backjoon_18222 - 투에-모스 문자열 - S2

문제
- 0과 1로 이루어진 길이가 무한한 문자열 X가 있다.
    1. X는 맨 처음에 "0"으로 시작한다.
    2. X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'를 만든다.
    3. X의 뒤에 X'를 붙인 문자열을 X로 다시 정의한다.
    4. 2~3의 과정을 무한히 반복한다.
- 즉, X는 처음에 "0"으로 시작하여 "01"이 되고, "01101001"이 되고, ... 의 과정을 거쳐 나타내어진다.
- 자연수 k가 주어졌을 때 X의 k번째에는 무슨 문자가 오는지 구하여라.
"""
# 0+0 = a , a+a' = b, b+b'=c, c+c'=d
# a[0] = 0, 
# 0  01  0110  01101001  0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0

def check_string(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    if num % 2 == 0:
        return check_string(num//2)
    else:
        return 1 - check_string(num//2)

k = int(input())

print(check_string(k-1))