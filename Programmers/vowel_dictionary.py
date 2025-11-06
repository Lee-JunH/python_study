"""
Programmers - 모음사전

문제
- 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

- 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

입출력 예
- 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA", "AAA", "AAAA", "AAAAA", "AAAAE", ... 와 같습니다. "AAAAE"는 사전에서 6번째 단어입니다.

풀이
- 일단 글자 수에 따라 숫자를 다르게?
- 예를 들어 보자
    - 길이가 1이고 A부터 시작하면 1로 시작 E면 ??
        - 길이가 2고 1 + 1해서 2로 E  
"""

def make_new(arr, word):
    text = ['A', 'E', 'I', 'O', 'U'] # 아에이오우 우하하하
    new_word = ''
    for a in arr:
        new_word += text[a]
    if new_word == word:
        return True
    return False

def solution(word):
    my_text = []

    count = 1
    for i in range(5):
        my_text.append(i)
        if make_new(my_text, word):
            return count
        count += 1
        for j in range(5):
            my_text.append(j)
            if make_new(my_text, word):
                return count
            count += 1
            for k in range(5):
                my_text.append(k)
                if make_new(my_text, word):
                    return count
                count += 1
                for l in range(5):
                    my_text.append(l)
                    if make_new(my_text, word):
                        return count
                    count += 1
                    for m in range(5):
                        my_text.append(m)
                        if make_new(my_text, word):
                            return count
                        count += 1
                        my_text.pop()
                    my_text.pop()
                my_text.pop()
            my_text.pop()
        my_text.pop()
    return count