"""
Backjoon_16967 - 배열 복원하기 - S3

문제
- H x W인 배열 A와 두 정수 X와 Y가 있을 때, 크기가 (H + X) x (W + Y)인 배열 B는
- 배열 A와 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을 겹쳐 만들 수 있다.
- 즉, 배열 B의 (i, j)에 들어있는 값은 아래 3개 중 하나이다.
    - (i, j)가 두 배열 모두에 포함되지 않으면, B(i,j) = 0 이다.
    - (i, j)가 두 배열 모두에 포함되면, B(i,j) = A(i,j) + A(i-X,j-Y)이다.
    - (i, j)가 두 배열 중 하나에 포함되면, B(i,j) = A(i,j) 또는 A(i-X,j-Y)이다.
- 배열 A는?

풀이
- 배열 B의 각 칸 B[i][j] = A[i][j] + A[i+X][j+Y] 이다.
- 또한 X, Y 가 1보다 크니까
- B의 [0][0:W] 는 A의 [0][0:W]와 같고 A의 [0][W:] 는 0이다.
- B의 [H+X-1][Y:W+Y-1] 은 A의 [H-1][Y:W-1]과 같고 [H-1][:Y]는 0이다.
- 즉 변한 부분은 (X,Y)부터 (H-X-1, W-Y-1) 까지만 변했다.
"""

H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = [[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]

for i in range(X, H):
    for j in range(Y, W):
        A[i][j] = B[i][j] - A[i-X][j-Y]

for i in range(H):
    print(*A[i])