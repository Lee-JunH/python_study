"""
문제
- Day of Mourning의 기타리스트 강토는 다가오는 공연에서 연주할 N개의 곡을 연주하고 있다.
- 이번 공연에서는 매번 곡이 시작하기 전에 볼륨을 바꾸고 연주하려고 한다.
- 먼저, 각각의 곡이 시작하기 전에 바꿀 수 있는 볼륨의 리스트를 만들었다.
- 이 리스트를 V라고 했을 때, V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다.
- 항상 리스트에 적힌 차이로만 볼륨을 바꿀 수 있다.
- 즉, 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, i번 곡은 P+V[i]나 P-V[i]로 연주해야 한다.
- 하지만, 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.
- 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 프로그램을 작성하시오.
- 모든 곡은 리스트에 적힌 순서대로 연주해야 한다.
- 연주할 수 없다면 -1 출력

조건
- 곡의 개수 : 1 <= N <= 50
- 시작 볼륨 : 0 <= S <= M, 1 <= M <= 1,000
"""

def volume_up_down(volume, idx):
    global result

    if volume < 0 or volume > M:
        return
    if idx == N:
        result = max(result, volume)
        return
    
    # 방문 체크로 시간 줄이기
    if vis[idx][volume]:
        return
    vis[idx][volume] = True

    volume_up_down(volume+V[idx], idx+1)
    volume_up_down(volume-V[idx], idx+1)
    

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

result = -1
vis = [[False for _ in range(M+1)] for _ in range(N+1)]

volume_up_down(S, 0)

print(result)