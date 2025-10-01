"""
2720 - 세탁소 사장 동혁
"""

T = int(input())
for _ in range(T):
    money = int(input())

    q = money // 25
    print(q, end=' ')
    money = money % 25
    print(money//10, end=' ')
    money %= 10
    print(money//5, end=' ')
    money %= 5
    print(money//1)