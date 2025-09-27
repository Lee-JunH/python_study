"""
SWEA_1849 - 영준이의 무게측정 - D6

문제
- 하루마다 N개의 새로운 샘플이 들어오고 오늘 하루는 이 N개의 샘플만 사용한다.
- 샘플에는 1~N까지의 번호가 붙어있다. 각 샘플은 정수 그램의 무게를 가진다.

풀이
- 딕셔너리에 값을 저장해서 차이를 출력한다.

- 
"""

def find(x):
    way = []
    while parent[x] != x:   # 부모 찾기
        way.append(x)
        x = parent[x]
    for sample in reversed(way):    # 부모를 찾는 동선
        weight[sample] += weight[parent[sample]]    # 무게 값 바꿔주기
        parent[sample] = x
    return x

def union(a, b, w):
    x = find(a)
    y = find(b)
    if x != y:
        parent[y] = x
        weight[y] = weight[a] + w - weight[b]

T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    measure = [list(input().split()) for _ in range(M)]

    weight = [0] * (N+1)
    parent = [x for x in range(N+1)]

    print(f'#{case+1}', end=' ')
    for i in range(M):
        op = measure[i][0]
        a = int(measure[i][1])
        b = int(measure[i][2])
        if op == '!':
            w = int(measure[i][3])
            union(a, b, w)
        elif op == '?':
            if find(a) != find(b):
                print('UNKNOWN', end=' ')
            else:
                print(weight[b] - weight[a], end=' ')
    print()

# T = int(input())
# for case in range(T):
#     N, M = map(int, input().split())
#     measure = [list(input().split()) for _ in range(M)]

#     weight = [[0 for _ in range(N)] for _ in range(N)]

#     print(f'#{case+1}', end=' ')
#     for i in range(M):
#         a = int(measure[i][1])
#         b = int(measure[i][2])
#         if measure[i][0] == '!':
#             w = int(measure[i][3])
#             weight[b] = weight[a] + w
#         else:
#             if a in weight and b in weight:
#                 print(weight[b] - weight[a], end=' ')
#             else:
#                 print('UNKNOWN', end=' ')
#     print()