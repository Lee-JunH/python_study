"""
주유소
"""

N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

cnt = 0
for i in range(len(dist)-1, -1, -1):
    cnt += min(price[0: i+1]) * dist[i]

print(cnt)