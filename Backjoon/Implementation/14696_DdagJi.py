"""
Backjoon_14696 - 딱지놀이 - B1

문제
- A, B가 딱지놀이를 한다. 이기는 조건은 다음과 같다.
    = 지면 뺨을 맞는다
    - 이기면 돈을 받고 오징어게임에 참여한다.
    - 공유는 잘 생겼다.
    - 별의 개수가 다를 때 별이 많은 쪽이 승
    - 별은 동일, 동그라미 개수가 많은 쪽이 승
    - 별, 동그라미 동일, 네모의 개수가 많은 쪽이 승
    - 별, 동그라미, 네모가 동일, 세모의 개수가 많은 쪽이 승
    - 모두 같다면 무승부 D
"""

def ddaggi():
    if a[0] > b[0]:
        compare = b[0]
    else:
        compare = a[0]
    
    for i in range(3, -1, -1):
        if shape_a[i] > shape_b[i]:
            return 'A'
        elif shape_a[i] < shape_b[i]:
            return 'B'
        else:
            continue
    return 0

N = int(input())
for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    shape_a = [0 for _ in range(4)]
    shape_b = [0 for _ in range(4)]

    for i in range(1, a[0]+1):
        shape_a[a[i]-1] += 1
    for i in range(1, b[0]+1):
        shape_b[b[i]-1] += 1

    result = ddaggi()
    if result == 0:
        print('D')
    else:
        print(result)