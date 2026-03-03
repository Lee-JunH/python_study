"""
Backjoon_1141 - 접두사 - S1

문제
- 접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합이다.
- 예를 들어, {hello}, {hello, goodbye, giant, hi}, 비어있는 집합은 모두 접두사X 집합이다.
- 하지만, {hello, hell}, {giant, gig, g} 는 접두사X 집합이 아니다.
- 단어 N개로 이루어진 집합이 주어질 때, 접두사X 집합인 부분집합의 최대 크기를 출력하시오.

조건
- N <= 50
- 단어 길이 <= 50
- 집합에는 같은 단어가 두 번 이상 있을 수 있다.
"""

N = int(input())
input_words = []
for i in range(N):
    word = input()
    input_words.append(word)

words = list(set(input_words))
new_N = len(words)
total = new_N

for i in range(new_N):
    len1 = len(words[i])
    for j in range(new_N):
        if i == j:
            continue
        len2 = len(words[j])
        if len1 <= len2:
            if words[i] == words[j][:len1]:
                total -= 1
                break

print(total)