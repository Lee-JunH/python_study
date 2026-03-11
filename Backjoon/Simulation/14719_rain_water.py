"""
Backjoon_14719 - 빗물 - G5

문제
- 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
- 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?
"""

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

result = 0
low_block = 0

for i in range(1, W-1):
    left = max(blocks[:i])
    right = max(blocks[i+1:])
    low_block = min(left, right)    # 지금 위치에서 왼쪽, 오른쪽을 봤을 때 가장 높은 값 중 낮은 값을 보고 계산
    
    if low_block > blocks[i]:
        result += low_block - blocks[i]
print(result)