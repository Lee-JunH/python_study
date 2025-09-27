"""
SWEA_5356 - 의석이의 세로로 말해요 - D3

문제
- 장난감에 영어 대문자, 소문자 숫자가 적혀있다. 이 글자들을 일렬로 붙여서 단어를 만든다.
- 5개의 단어를 만들고 세로로 읽으려 한다.
- 해당 자리가 없으면 읽지 않고 다음 글자를 계속 읽는다.

풀이
- 구현문제
"""

T = int(input())
for case in range(T):
    words = [list(input().strip()) for _ in range(5)]

    max_length = 0
    for word in words:
        max_length = max(max_length, len(word))

    print(f'#{case+1}', end=' ')
    for i in range(max_length):
        for j in range(5):
            if len(words[j]) > i:
                print(words[j][i], end='')
    print()