"""
Backjoon_1325 - 효율적인 해킹 - S1

문제
- 어느 회사를 해킹하려 하는데 이 회사는 N개의 컴퓨터로 이루어져 있다.
- 한 번의 해킹으로 여러 개의 컴퓨터를 해킹할 수 있는 컴퓨터를 해킹하려 한다.
- 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데,
  A가 B를 신뢰하는 경우에는 B를 해킹하며느 A도 해킹할 수 있다는 소리다.
- 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때,
  한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 만드시오.
"""

N, M = map(int, input().split())
trust_node = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    trust_node[B].append(A)

result = []
for i in range(1, N+1):
    trust = [i]
    cnt = 0
    vis = [0 for _ in range(N+1)]
    vis[i] = 1
    while trust:
        num = trust.pop()
        for t in trust_node[num]:
            if not vis[t]:
                trust.append(t)
                vis[t] = 1
                cnt += 1
    result.append(cnt)

max_com = max(result)
for i in range(N):
    if result[i] == max_com:
        print(i+1, end=' ')