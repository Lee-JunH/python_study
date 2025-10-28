"""
Backjoon_1676 - 팩토리얼 0의 개수 - S5

문제
- N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 문제
"""

N = int(input())

factorial = 1
for i in range(N):
    factorial *= i+1

count = 0
new_str = list(str(factorial))
new_str.reverse()
for n in new_str:
    if n != '0':
        break
    count += 1
print(count)