"""
backjoon_12865 - 평범한 배낭 - G5

문제
- 여행에 필요하다고 생각하는 N개의 물건이 있다.
- 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있다.
- 배낭에 최대 K만큼의 무게를 넣을 수 있을 때, 물건들의 가치 최댓값을 구하라.

출력
- 배낭에 넣을 수 있는 물건들의 가치합의 최댓값

풀이
- 무게 W인 물건들의 합이 K보다 작을 때 V합의 최댓값을 구해야 한다.
- 모든 경우의 수를 하면 시간이 오래 걸릴 것 같다. (A형도 시간 초과 났었음..)
- 
"""

N, K = map(int, input().split())
baggage = [tuple(map(int, input().split())) for _ in range(N)]

bag = []
for i in range(N):
    bag.append(baggage[i])
    if sum() < K:
        pass