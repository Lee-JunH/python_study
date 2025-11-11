"""
Backjoon_28279 - 덱 2 - S4

문제
- 정수를 저장하는 덱을 구현한 다음, 명령을 처리하는 프로그램 작성하기
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
my_deque = deque()

for _ in range(N):
    command = list(map(int, input().split()))

    if command[0] == '1':
        my_deque.appendleft(int(command[1]))

    elif command[0] == '2':
        my_deque.append(int(command[1]))

    elif command[0] == '3':
        if my_deque:
            print(my_deque.popleft())
        else:
            print(-1)

    elif command[0] == '4':
        if my_deque:
            print(my_deque.pop())
        else:
            print(-1)

    elif command[0] == '5':
        print(len(my_deque))

    elif command[0] == '6':
        if my_deque:
            print(0)
        else:
            print(1)

    elif command[0] == '7':
        if my_deque:
            print(my_deque[0])
        else:
            print(-1)

    elif command[0] == '8':
        if my_deque:
            print(my_deque[-1])
        else:
            print(-1)