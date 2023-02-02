#인접 행렬로 문제 풀이 -> 공간복잡도상 인접 리스트가 효율적

from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visit[v] = 0
    while (queue):
        v = queue[0]
        print(v, end=' ')
        queue.popleft()
        for i in range(1, n + 1):
            if visit[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)