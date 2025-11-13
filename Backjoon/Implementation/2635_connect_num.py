# baekjoon_2635 - 수 이어가기 - S5

num = int(input())
count_max = 0
result = 0
for i in range(num, -1, -1):
    count = 2
    temp1 = num
    temp2 = i
    while temp1 - temp2 >= 0:
        temp = temp1 - temp2
        temp1 = temp2
        temp2 = temp
        count += 1
    if count_max <= count:
        count_max = count
        result = i

lst = [num, result]
i = 0
while True:
    if lst[i] - lst[i+1] < 0:
        break
    lst.append(lst[i]-lst[i+1])
    i += 1
print(count_max)
print(' '.join(str(n) for n in lst))