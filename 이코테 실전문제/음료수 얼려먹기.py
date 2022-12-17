# 이코테 151p

# dfs의 경우 스택을 사용한다. 그냥 append 사용하면 됨, 혹은 재귀함수 사용
# 묶음을 찾아주는 프로그램

#1. 특정 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아진 방문하지 않은 지점이 있다면 해당 지점을 방문한다.
#2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 다시 진행하면, 연결된 모든 지점을 방문할 수 있다.
#3. (1), (2)번의 과정을 모든 노드에 반복하며 방문하지 않은 지점의 수를 센다.

n, m = map(int, input().split())
# graph = [i for i in list(map(int, input()))] #얼음 트레이 

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 
  if x <= -1 or n >= n or y <= -1 or y >= m:
    return False

  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x - 1, y)
    dfs(x + 1, y)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)