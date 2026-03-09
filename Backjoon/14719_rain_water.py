"""
Backjoon_14719 - 빗물 - G5

문제
- 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
- 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?
"""

def count_block(st):
    hap = 0
    for block in st:
        hap += high_b - block
    return hap

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

result = 0
high_b = 0
my_stack = []

for i in range(W):
    if i == W - 1:
        if my_stack:
            if blocks[i] < high_b:
                high_b = blocks[i]
            result += count_block(my_stack)
        break

    if high_b == 0:     # 첫 값 입력
        high_b = blocks[i]
    else:  
        if blocks[i] >= high_b:
            if my_stack:
                result += count_block(my_stack)
                my_stack.clear()
            high_b = blocks[i]
        elif blocks[i] < high_b:
            my_stack.append(blocks[i])

print(result)