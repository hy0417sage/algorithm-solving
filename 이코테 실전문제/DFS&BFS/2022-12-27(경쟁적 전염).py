# 바이러스 K가지
# 바이러스는 1초마다 상 하 좌 우 방향으로 증식한다.
# 번호가 낮은 종류의 바이러스부터 먼저 증식
# 증식 과정에서 바이러스가 있다면 증식 할 수 없다.
## S초가 지난 후 (3, 2)에 존재하는 바이러스의 종류를 계산해 보자

n, k = map(int, input().split())
lab = []
for _ in range(n):
  lab.append(list(map(int, input().split())))
s, x, y = map(int, input().split()) #s초가 지난후에 (x, y)에 존재하는 바이러스는?

# 바이러스를 퍼트리기 위해
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

temp = [[0]*n for i in range(n)]
for i in range(n):
  for j in range(n):
    temp[i][j] = lab[i][j]

# 바이러스를 검사한다. 1부터 K까지 수를 확인하고 바이러스를 감염 시킨다.
def virus(x, y, num):
  global temp
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if lab[nx][ny] == 0:
        temp[nx][ny] = num #바이러스가 없을 경우 바이러스 num을 위치시킨다.
  print(temp)

def secVirus():
    # 1부터 K까지 수를 확인하고 바이러스를 감염 시킨다. (1초당)
    for virusNum in range(0, k + 1):
      for x in range(n):
        for y in range(n):
          if lab[x][y] == virusNum:
              virus(x, y, virusNum)
            
      for i in range(n):
        for j in range(n):
          lab[i][j] = temp[i][j]

for _ in range(s):
    secVirus() # s초만큼 바이러스 감염 시키고
print(lab[x-1][y-1])