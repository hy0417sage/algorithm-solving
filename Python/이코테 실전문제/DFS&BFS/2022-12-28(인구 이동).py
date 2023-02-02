# N * N 크기의 땅
# 각각의 땅에는 나라가 하나씩 존재함
# r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
#####인구이동####
# 1. 국경선을 공유하는 두 나라의 인구차이가 (L이상) (R 이하)라면 두 나라가 공유하는 국경선을 하루동안 안연다. (1 조건을 판단하는 함수 canOpenBorder)
# 2. 위 조건에 의해 열어야 하는 국경선이 모두 열렸다면, 인구 이동을 시작한다. 
    # 3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 하루동안 연합이라고 한다. (dx, dy 방향 리스트 만들기)
    # 4. 연합을 이루는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 인구수)가 된다. !소수점은 편의상 버린다! (2 연합의 인구수를 계산하는 함수 만들기 counting)
# 5. 연합을 해제하고, 모든 국경선을 닫는다.

# 1. 전체 검사하기 연합이 가능하면 True, 불가능 하면 flase
# 2. 검사된 결과로 (1)True 카운팅 (2)True 이면 연합 인구수 계산
# 3. 결과 result 카운팅 하기! 

n, l, r = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))

dx, dy = [0, -1], [1, 0]
state = [[False] * n for _ in range(n)]


# 국경이 열렸을 경우 True
def canOpenBorder(x, y):
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if l <= abs(country[x][y] - country[nx][ny]) <= r:
                state[x][y], state[nx][ny] = True, True


def populationCounting(population, association):
    return int(population / association) #연합 인구수, 연합 칸의 계수

population, count = 0, 0

# 연합국 갯수와 인구 수 계산
def dfs(x, y):
    if 0 <= x < n and 0 <= y < n:
        if state[x][y] == True:
            state[x][y] = False
            population += country[x][y]
            country[x][y] = -1
            count += 1
            dfs(x, y-1)
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)

answer = 0

def solution(moveCount):
    #국경을 열 수 있는지 확인
    for i in range(n):
        for j in range(n):
            canOpenBorder(i, j)
    dfs(0, 0)
    result = populationCounting(population, count)

    if count == 0:
        return answer

    for i in range(n):
        for j in range(n):
            if country[i][j] == -1:
                country[i][j] = result
    answer += 1

    


print(solution(0))

