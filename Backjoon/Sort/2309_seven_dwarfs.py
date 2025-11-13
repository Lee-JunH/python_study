# Backjoon_2309 - 일곱 난쟁이 - B1

dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

find = sum(dwarfs) - 100
dwarfs.sort()

for i in range(8):
    for j in range(i+1, 9):
        if dwarfs[i] + dwarfs[j] == find:
            break
    if dwarfs[i] + dwarfs[j] == find:
            break
for k in range(9):
    if k == i or k == j:
        continue
    print(dwarfs[k])