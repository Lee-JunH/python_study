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
# n : 트럭의 수, w : 다리길이, L : 다리 최대 하중
n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

#다리 크기 만큼의 리스트를 만들고 하나씩 append하면서 최대 중량 안넘게 하기

bridge = deque([0] * w) # 다리 길이 크기의 리스트
time = 0

while bridge:
    time += 1
    bridge.popleft()

    if trucks:  # 트럭이 남아 있으면
        if sum(bridge) + trucks[0] < L:    # 다리에 올릴 수 있는지 확인
            new_truck = trucks.popleft()    # 올릴 트럭
            bridge.append(new_truck)    # 다리에 올리기
        else:
            bridge.append(0)
print(time)