# baekjoon_2116 - 주사위 쌓기 - G5


def find_max(dice, bottom):     # 옆면이 갖는 최대 값 찾는 함수
    for num in range(6):    # 바닥값의 index 찾기
        if dice[num] == bottom:
            break
    if num == 0:
        return (dice[5], max(dice[1], dice[2], dice[3], dice[4]))
    elif num == 1:
        return (dice[3], max(dice[0], dice[2], dice[4], dice[5]))
    elif num == 2:
        return (dice[4], max(dice[0], dice[1], dice[3], dice[5]))
    elif num == 3:
        return (dice[1], max(dice[0], dice[2], dice[4], dice[5]))
    elif num == 4:
        return (dice[2], max(dice[0], dice[1], dice[3], dice[5]))
    elif num == 5:
        return (dice[0], max(dice[1], dice[2], dice[3], dice[4]))


num = int(input())
dice = [list(map(int, input().split())) for _ in range(num)]
result = 0


for i in range(1, 7):   # 모든 바닥 값에 대한 경우의 수를 찾는다.
    dice_bottom = i
    sum_dice = 0
    for j in range(num):   # 각 주사위에 대해서 실행
        dice_bottom, dice_max = find_max(dice[j], dice_bottom)
        sum_dice += dice_max    # 옆면의 max값 더하기
    result = max(result, sum_dice)
print(result)
