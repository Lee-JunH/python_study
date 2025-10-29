# baekjoon_1244 - 스위치 켜고 끄기 - S4

test_case = int(input())

switch = [int(x) for x in input().split()]

student = int(input())

def change(switch, a):
    if switch[a] == 0:
        switch[a] = 1
    else:
        switch[a] = 0


for _ in range(student):
    gen, num = map(int, input().split())
    if gen == 1:
        i = 1
        while num * i - 1 < test_case:
            change(switch, num * i - 1)
            i += 1
    elif gen == 2:
        i = 1
        while 0 <= num - 1 - i and num - 1 + i < test_case:
            if switch[num - 1 - i] == switch[num - 1 + i]:
                i += 1
            else:
                break
        for j in range(num - 1 - (i - 1), num - 1 + (i - 1) + 1):
            change(switch, j)

for i in range(test_case):
    if i % 20 == 0 and i != 0:
        print()
    print(switch[i], end=' ')
