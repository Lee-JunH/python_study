# backjoon_2491 - 수열 - S4

N = int(input())
lst = list(map(int, input().split()))

count = 0
max_count1 = 0
temp = lst[0]
for i in range(N):
    if temp <= lst[i]:
        count += 1
    else:
        count = 1
    if max_count1 < count:
            max_count1 = count
    temp = lst[i]

lst2 = lst[::-1]
count = 0
max_count2 = 0
temp = lst2[0]
for i in range(N):
    if temp <= lst2[i]:
        count += 1
    else:
        count = 1
    if max_count2 < count:
            max_count2 = count
    temp = lst2[i]

print(max(max_count1, max_count2))