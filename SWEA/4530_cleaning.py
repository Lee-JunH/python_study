"""
SWEA_4530 - 극한의 청소 작업 - D4

문제
- 민기는 지하 999,999,999,999 층에서 지상 999,999,999,999층에 이르는 거대한 건물을 건설했다.
- 4라는 숫자가 들어간 모든 층을 건너뛰어 건설하였다.
- 0층은 존재하지 않는다.
- 은비는 청소를 위해 A층에서 B층으로 올라가려고 한다. 몇 층을 올라가야 하는가?

풀이
- 일반적인 반복문은 이중 반복문을 사용해야해서 시간초과가 발생한다.
- 그럼 반복문을 한번 사용해서 구하는 방법은?
    - 4가 있는 경우를 어떻게 찾을 수 있을까?
- 1~10은 9개, 11~20은 9개 ,..., 31~39, 50~60, ...
- 즉 2자리 조합에서 9개 짜리가 9세트 있다. 9의 1제곱
"""

def count_four(num):
    count = 0   # 개수 세기
    gop = 0     # 자리수 
    num = abs(num)
    while num > 0:
        remain = num % 10   # 끝자리(나머지)
        num = num // 10   # 몫S
        if remain >= 4:
            count += (remain - 1) * (9 ** gop)
        else:
            count += remain * (9 ** gop)
        gop += 1
    return count


T = int(input())
for case in range(T):
    A, B = map(int, input().split())
    
    a = count_four(A)
    b = count_four(B)

    if A < 0 < B:
        result = a + b - 1
    else:
        result = abs(b - a)
    print(f'#{case+1} {result}') 