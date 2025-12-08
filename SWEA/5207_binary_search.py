"""
SWEA_5207 - 이진 탐색 - D3

문제
- 서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다.
- 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 하려 한다.
- 전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고,
- 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.
- M개의 정수 중 조건을 만족하는 정수의 개수를 구하시오.
"""

# check의 역할은 오른쪽 왼쪽 중 어느 곳을 봤는지 저장하는 변수
def bin_search(l, r, check):
    global cnt2

    if l > r:   # 왼쪽이 더 크면 잘못된 경우
        return 0
    
    m = (l+r) // 2      # 중앙 값
    if l == r:      # 같을 때
        if A[m] == find: # 그 자리가 구하는 값이면
            return 1
        return 0
    
    if A[m] < find:     # 찾는 값보다 중앙값이 작으면
        if check == 1:
            cnt2 = 0
        return bin_search(m+1, r, 1)    # 중앙부터 다시 시행
    elif A[m] > find:   # 찾는 값보다 중앙값이 크면
        if check == 0:
            cnt2 = 0
        return bin_search(l, m-1, 0)
    else:   # 중앙값이 찾는 값인 경우
        return 1

T = int(input())
for case in range(T):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    cnt = 0
    for i in range(M):
        find = B[i]
        cnt2 = 1
        if bin_search(0, N-1, 2):
            if cnt2 == 1:
                cnt += 1
    print(f'#{case+1} {cnt}')