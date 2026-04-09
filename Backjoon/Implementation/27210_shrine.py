"""
Backjoon_27210 - 신을 모시는 사당 - G5

문제
- 신을 모시는 사당에는 신을 조각한 돌상 N개가 일렬로 놓여 있다. 각 돌상은 왼쪽 또는 오른쪽을 바라보고 서있다.
- 연속한 몇 개의 돌상에 금칠을 하여 궁극의 깨달음을 얻고자 한다.
- 궁극의 깨달음을 얻기 위해서는 가능한 한 많은 금색 돌상들이 같은 방향을 바라보아야 한다.
- 방향이 다른 돌상은 깨달음에 치명적이다. 깨달음의 양은 아래와 같다.
    - |(왼쪽을 바라보는 금색 돌상의 수) - (오른쪽을 바라보는 금색 돌상의 개수)|
- 궁극의 깨달음을 얻을 수 있을까?
- (왼쪽: 1, 오른쪽: 2)
"""

N = int(input())
statue =  list(map(int, input().split()))

max_left = 0
sum_left = 0

max_right = 0
sum_right = 0

for i in statue:
    if i == 1:
        sum_left += 1
        sum_right -= 1
    else:
        sum_left -= 1
        sum_right += 1

    if sum_left < 0:
        sum_left = 0
    if sum_right < 0:
        sum_right = 0

    if sum_left > max_left:
        max_left = sum_left
    if sum_right > max_right:
        max_right = sum_right

print(max(max_right, max_left))
