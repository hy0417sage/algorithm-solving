# 벽을 3개 설치하는 모든 경우의 수를 가 계산해야 한다.
n, m = 7. 8
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safeScore = 0

dfs(0)
print(result)

# 바이러스 퍼트리게 하는 함수
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전지대 계산
def safeScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# dfs
def dfs(start):
    global resultScore

    if count == 3: # 울타리가 3개라면
        for i in range(n):
            for j in range(m):
                data[i][j] = temp[i][j]
        for i in range(n):
            for j in range(m):
                if data[i][j] == 2:
                    virus(i, j)
        safeScore = max(resultScore, safeScore()) 



































# # 깊이 우선 탐색 DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dx[i]
#         # 상하좌우 바이러스가 사방으로 퍼지도록 하기
#         if 0 <= nx < n and 0 <= ny < m:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = 2:
#                 virus(nx, ny)

# # 현재 맵에서 안전 영역의 크기 계산하는 메서드
# def getScore():
#     score = 0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j] == 0:
#                 score += 1
#     return score

# # 깊이 우선 탐색을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
# def dfs(count):
#     global result
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = data[i][j]
#         # 각 바이러스의 위치에서 전파 진행
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i, j)
#         result = max(result, getScore())
#         return

#     # 빈 공간에 울타리 설치
#     for i in range(n):
#         for j in range(m):
#             if data[i][j] == 0:
#                 data[i][j] = 1
#                 count += 1
#                 dfs(count)
#                 data[i][j] = 0
#                 count -= 1