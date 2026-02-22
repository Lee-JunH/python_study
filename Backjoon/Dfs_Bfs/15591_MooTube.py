"""
Backjoon_15591 - MooTube(Silver) - G5

문제
- 농부 존은 MooTube라 불리는 동영상 공유 서비스를 만들었다.
- 소들은 N개의 동영상을 이미 올려 놓았다.
- 소들이 좋아할만한 동영상을 찾을 수 있게 "연관 동영상"리스트를 만들었다.
- N-1개의 동영상 쌍을 골라서 직접 두 쌍의 USADO를 계산했다.
- 임의의 두 쌍 사이의 동영상의 USADO를 그 경로의 모든 연결들의 USADO중 최솟값으로 하기로 했다.
- 값 K를 정해, USADO가 K 이상인 모든 동영상이 추천되도록 할 것이다.
- 어떤 K 값에 대해 추천 동영상의 개수를 답하시오.
"""

def bfs(k, v):
    vis = [0 for _ in range(N+1)]
    vis[v] = 1
    cnt = 0
    my_l = [(v, float('inf'))]

    while my_l:
        video, usado = my_l.pop()
        for video_n, usado_n in node[video]:    # 다음 비디오와 유사도 확인
            usado_n = min(usado, usado_n)       # 값은 현재와 다음값의 min 값
            if usado_n >= k and not vis[video_n]:   # k보다 크면
                cnt += 1
                my_l.append((video_n, usado_n))
                vis[video_n] = 1
    return cnt

N, Q = map(int, input().split())
node = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())

    node[p].append((q,r))
    node[q].append((p,r))

for i in range(Q):
    k, v = map(int, input().split())
    
    print(bfs(k, v))