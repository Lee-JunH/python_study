"""
SWEA_5204 - 병합정렬 - D3

문제
- N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.
- 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
- 정렬이 끝난 리스트 L에서 L[N//2]원소를 출력한다.
"""

def merge_sort(a):
    global cnt

    if len(a) == 1:   # 한 개만 남았을 때 그 값 리턴
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])  # 왼쪽은 처음부터 중간까지
    right = merge_sort(a[mid:]) # 오른쪽은 중간부터 끝까지

    if left[-1] > right[-1]:    # 왼쪽 끝값이 오른쪽 끝값보다 클 때 count
        cnt += 1

    l = 0
    r = 0
    result = []
    while l < len(left) or r < len(right):
        if l == len(left):
            result.append(right[r])
            r += 1
        elif r == len(right):
            result.append(left[l])
            l += 1
        elif left[l] > right[r]:
            result.append(right[r])
            r += 1
        elif left[l] <= right[r]:
            result.append(left[l])
            l += 1
    return result

T = int(input())
for case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    merge_sort(arr)
    print(f'#{case+1} {arr[N//2 - 1]} {cnt}')