# Backjoon_10158 - 개미 - S3

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 왓다 갓다를 반복문 없이 구현하자 0 1 2 3 2 1 0 이런식으로 바뀌니까
p = (p+t) % (2*w)
if p > w:
    p = w - (p-w)   # 차이만큼 빼주기

q = (q+t) % (2*h)
if q > h:
    q = h - (q-h)   # 차이만큼 빼주기

print(f'{p} {q}')


# 시간 초과
# # x좌표는 주기적으로 움직인다 4 -> 5 -> 6 -> 5 -> 4 -> 3 ...
# dir = 1
# for _ in range(t):
#     if p == w:
#         dir = -1
#     elif p == 0:
#         dir = 1
#     p += dir

# # y좌표도 주기적으로 움직인다. 1->2->3->4->3->2->1->,,,
# dir = 1
# for _ in range(t):
#     if q == h:
#         dir = -1
#     elif q == 0:
#         dir = 1
#     q += dir

# print(f'{p} {q}')