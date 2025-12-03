"""
Backjoon_4811 - 알약 - G5

문제
- 매일 약 반알을 먹는다.
- 약이 N개 담긴 병이 있을 때
- 첫째 날에 병에서 약 하나를 꺼내고 약을 반으로 쪼개서 한 조각 먹고, 다른 조각은 다시 병에 넣는다.
- 한 조각을 꺼낸 날에는 W를, 반 조각을 꺼낸 날에는 H를 보낸다.
- 문자를 종이에 기록할 때, 총 2N일이 지나면 길이가 2N인 문자열이 만들어지게 된다.
- 가능한 서로 다른 문자열의 개수는 총 몇개인가?

풀이
- 처음에는 무조건 하나
- 그 다음부터 하나 or 반
- 근데 반을 꺼내면 다음은 무조건 하나인 경우도 있음
- 반대로 하나만 계속 꺼내서 반만 남는 경우도 있음
- 이 모든 경우의 수를 세야 한다.
"""
# from math import comb

# def catalan(n):
#     return comb(2*n, n) // (n + 1)

# for i in range(1000):
#     a = int(input())
#     if a == 0:
#         exit()
#     print(catalan(a))


arr = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    arr[0][i] = 1
for i in range(1, 31):
    for j in range(i, 31):
        arr[i][j] += arr[i-1][j] + arr[i][j-1]
while True:
    N = int(input())
    if N == 0:
        break
    print(arr[N][N])