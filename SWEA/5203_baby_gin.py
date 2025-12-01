"""
SWEA_5203 - 베이비진 게임 - D3

문제
- 0~9 까지의 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때
- 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
- 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.
- 두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자는?
"""

def check_same(p):
    for i in range(10):
        if p[i] >= 3:
            return 1
    return 0

def check_sequence(p):
    for i in range(8):
        check = 0
        for j in range(i, i+3):
            if p[j] >= 1:
                check += 1
        if check == 3:
            return 1
    return 0


T = int(input())
for case in range(T):
    card = list(map(int, input().split()))

    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            player1[card[i]] += 1
            if len(player1) >= 3:
                if check_same(player1) or check_sequence(player1):
                    winner = 1
                    break
        else:
            player2[card[i]] += 1
            if len(player2) >= 3:
                if check_same(player2) or check_sequence(player2):
                    winner = 2
                    break
    print(f'#{case+1} {winner}')