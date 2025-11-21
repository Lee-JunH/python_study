"""
SWEA_5201 - 컨테이너 운반 - D3

문제
- 화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
- 트럭 당 한 개의 컨테이너를 운반할 수 있고, 트럭의 적재용량을 초과 불가
- A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다.
- 이동한 화물의 총 중량이 최대가 되도록 옮겼다면, 옮겨진 화물의 전체 무게는 얼마?
"""

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort()
    containers.reverse()    # 내림차순으로 정렬하기

    weight = 0
    vis = [0 for _ in range(N)]     # 이동 여부 체크하기
    for t in range(M):
        for c in range(N):
            # 트럭 용량과 제일 비슷한 거  먼저 옮기기
            if not vis[c] and trucks[t] >= containers[c]:
                weight += containers[c]
                vis[c] = 1
                break
    print(f'#{case+1} {weight}')