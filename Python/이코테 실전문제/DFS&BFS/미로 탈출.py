# 이코테 154p

from collections import deque 
# 시작이 1, 1
# 탈출구 N, M
# 괴물부분 0, 없는 부분 1
# 시작칸, 마지막칸 포함하여 계산

# 1. 입력 받기
n, m = map(int, input().split())
load_map = []

dx = [0, 1, -1, 0] # 상, 우, 하, 좌
dy = [-1, 0, 0, -1]

for _ in range(n):
  load_map.append(list(map(int, input())))

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
  
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위를 벗어났을 경우
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 벽이 있을 경우
      if load_map[nx][ny] == 0:
        continue
      # 공간이 있을 경우 (go)
      if load_map[nx][ny] == 1:
        load_map[nx][ny] = load_map[x][y] + 1
        queue.append((nx, ny))
        
  return load_map[n-1][m-1]

print(bfs(0, 0))
