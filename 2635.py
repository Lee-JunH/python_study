# 수 이어가기

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
    count_max = max(count_max, count)
    if count_max == count: result = i

print(count_max)
temp1 = num
temp2 = result
print(num, end = ' ')
print(result, end = ' ')
while temp1 - temp2 >= 0:
    temp = temp1 - temp2
    temp1 = temp2
    temp2 = temp
    print(temp, end = ' ')