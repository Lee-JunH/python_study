"""
Backjoon_5430 - AC - G5

문제
- AC는 정수 배열에 연산을 하기 위해 만든 언어이다.
- 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
- 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다.
- 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
"""


from collections import deque
import json

def print_lst(arr):
    length = len(arr)

    print('[', end='')
    for i in range(length):
        print(arr[i], end='')
        if i != length-1:
            print(',', end='')
    print(']')

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    lst = json.loads(input())
    lst = deque(lst)

    error = False
    rev = 0
    for command in p:
        if command == 'R':
            rev += 1
        elif command == 'D':
            if not lst:
                error = True
                break
            if rev % 2 == 0:
                lst.popleft()
            else:
                lst.pop()
    if error:
        print('error')
    else:
        if rev % 2 == 1:
            lst.reverse()
        print_lst(lst)