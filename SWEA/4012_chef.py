"""
SWEA_4012 - 요리사 - 모의 SW 역량테스트

문제
- N개의 식재료를 N/2개씩 나누어 2개의 요리를 하려고 한다.
- A음식과 B음식의 맛 차이가 최소가 되도록 재료를 배분해야 한다.
- 식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다.

풀이
- N개의 식재료가 있고 N/2개 골라서 만들 수 있는 모든 조합을 구해서 리스트에 저장하자.
- 저장해서 서로 차를 구해서 차가 가장 작은 걸 출력하면 되잖어~

- 되기는 무슨 안됨
- 남은 걸로 계산해서 빼야하기 때문에 visited 같은 걸로 썼는지 체크 하고 안쓴 걸로 조합 하기

예시
- 4개인 경우 2개를 골라야 해.
- 1 2를 선택하면 3 4가 나머지
- arr[1][2] 랑 arr[2][1]
- arr[3][4] 랑 arr[4][3]

6개 인 경우 -> 모든 경우의 수는 6C3 인데 10개 까지만 계산하면 나머지는 순서만 다른 경우이다.


"""

def taste(food):        # 재료 조합하기
    mat = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            ingredient1 = food[i]-1
            infredient2 = food[j]-1
            mat += arr[ingredient1][infredient2] + arr[infredient2][ingredient1]
    return mat

def calculate(food1, food2):   #   재료 조합하기
    global min_cha

    taste1 = taste(food1)
    taste2 = taste(food2)

    cha = abs(taste1 - taste2)
    min_cha = min(min_cha, cha)

def dfs(start, cnt):       # 재료 선택하기
    if cnt == N//2:
        food2 = [i for i in range(1, N+1) if not visited[i]]
        calculate(food1, food2)
        return

    for i in range(start+1, N+1):
        food1.append(i)
        visited[i] = True
        dfs(i, cnt+1)
        food1.pop()
        visited[i] = False

T = int(input())
for case in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cha = float('inf')
    visited = [0 for _ in range(N+1)]
    food1 = [1]       # 음식 조합 담아둘 곳
    visited[1] = True

    dfs(1, 1)
    
    print(f'#{case+1} {min_cha}')