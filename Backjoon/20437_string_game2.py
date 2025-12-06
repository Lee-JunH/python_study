"""
Backjoon_20437 - 문자열 게임2 - G5

문제
- 게임의 진행 방식
    - 알파벳 소문자로 이루어진 문자열 W가 주어진다.
    - 양의 정수 K가 주어진다.
    - 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
    - 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
- 이 방식으로 게임을 T회 진행한다.
"""

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())

    min_string = 10000
    max_string = 0

    words = [0 for _ in range(26)]      # 문자 수 세는 리스트
    words_idx = [[] for _ in range(26)]  # 길이 세는 리스트
    for i in range(len(W)):
        num = ord(W[i]) - 97
        words[num] += 1
        words_idx[num].append(i)
    
    check = False
    for i in range(26):
        if words[i] >= K:
            check = True
            for j in range(len(words_idx[i]) - K + 1):
                new_arr = words_idx[i][j:j+K]
                min_string = min(min_string, new_arr[-1] - new_arr[0] + 1)
                max_string = max(max_string, new_arr[-1] - new_arr[0] + 1)
    
    if check:
        print(f'{min_string} {max_string}')
    else:
        print(-1)