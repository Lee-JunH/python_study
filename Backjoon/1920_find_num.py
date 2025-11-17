"""
Backjoon_1920 - 수 찾기 - S4

문제
- N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하면 1, 아니면 0
"""

N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

for i in range(M):
    if M_lst[i] in N_lst:
        print(1)
    else:
        print(0)