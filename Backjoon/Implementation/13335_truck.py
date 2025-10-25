"""
Backjoon_13335 - 트럭 - S1

문제
- 하나의 차선으로 된 다리가 하나 있다. 이 다리를 n개의 트럭이 건러가려고 한다.
- 다리 위는 w대의 트럭만 동시에 올라갈 수 있다. 다리의 길이는 w 단위길이이며,
- 각 트럭들은 하나의 단위시간에 하나의 단위길이만큼 이동 가능하다.
- 동시에 올라가는 트럭들의 무게 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

풀이
- 다리에 올릴수 있는지 없는지로 나눠서 생각한다.
- 1. 올라갈 수 있는 경우
    - 트럭 무게확인 후 다리에 올리기
- 2. 더이상 못올라가는 경우
    - 다리 위에 있는 트럭 하나를 뺀다.
"""

from collections import deque

n, w, L = map(int, input().split())
truck = deque(list(map(int, input().split())))

bridge = deque([0] * w)    # 다리 위 정보
time = 0    # 시간 저장

while bridge:   # 다리 위에 트럭이 없을 때 까지
    time += 1
    bridge.popleft()    # 한칸 씩 왼쪽으로 옮기기

    # 트럭이 안남아 있으면 왼쪽으로 계속 옮기기
    if truck:
        if sum(bridge) + truck[0] <= L: # 트럭 더 올리고 한칸 이동
            new_truck = truck.popleft()
            bridge.append(new_truck)
        else:
            bridge.append(0)    # 한칸 이동
print(time)