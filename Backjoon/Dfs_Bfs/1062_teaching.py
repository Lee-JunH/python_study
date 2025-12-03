"""
Backjoon_1062 - 가르침 - G4

문제
- K개의 글자를 가르칠 시간 밖에 없다.
- 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다.
- 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 구하는 문제
- 남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다.
- 단어는 N개 밖에 없다고 가정하고 읽을 수 있는 단어의 최댓값은?
"""

import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global max_word

    if cnt == K-5:  # 다 했으면 확인
        complete = 0
        for word in words:
            for w in word:
                temp = True
                if not teach[ord(w) - 97]:
                    temp = False
                    break
            if temp:
                complete += 1
        max_word = max(max_word, complete)
        return
    
    for i in range(idx, 26):
        if not teach[i]:
            teach[i] = 1
            dfs(i, cnt+1)
            teach[i] = 0


N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

teach = [0] * 26

if K < 5:   # 필수 a, v, i, n, t
    print(0)
    exit()

for i in ('a', 'c', 'i', 'n', 't'):
    teach[ord(i)-97] = 1

max_word = 0
dfs(0, 0)

print(max_word)