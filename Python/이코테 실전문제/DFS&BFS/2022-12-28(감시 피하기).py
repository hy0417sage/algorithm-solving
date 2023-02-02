# N * N 크기의 복도
# 선생님(T), 학생(S), 장애물(O)
# 복도에 나온 학생들이 선생님의 감시에 들키지 않는 것이 목표
# 선생님은 상하좌우 감시 / 단, 복도에 장애물이 있으면 학생을 볼 수 없음(장애물로 막히기 전까지 볼 수 있음)
# 학생들은 3개의 장애물을 설치한다. 결과로 모든 학생이 감시를 피할 수 있어야 한다.
# 3개의 장애물로 모든 학생이 선생님의 감시를 피할 수 있는지 출력하기!
# 전역변수를 많이 사용하면 안되는 이유 : 함수 하나의 변경 사항이 다른 함수의 변경 사항에 영향이 많이 감

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(str, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 특정 방향으로 검사 진행(안들킴 : True, 들킴 : False)
def SuccessAvoiding(x, y):
    avoiding = True
    for i in range(4):
        if not avoiding:
            return False
        avoiding = avoidingCheck(x, y, i)
    return True

# 선생님의 시야에 학생이 있는지 검사하기
# 학생이 선생님께 한번이라도 들켰을 경우 False, 모든 학생들이 성공했을 경우 True
def avoidingCheck(x, y, i):
  while True:
    x += dx[i]
    y += dy[i]
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 'S':
            return False
    else:
      return True

obstacle = 0
result = 'Yes'
# 모든 경우의 수를 계산하여 최종적으로 True를 반환하면 성공!
def solution(x, y):
    global obstacle, result
    if obstacle == 3: #####그냥 변수로 수정
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T': #선생님이 있는 위치 확인
                    if not SuccessAvoiding(i, j): #감시가 한번이라도 실패하면
                        result = 'No'
                        return
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                obstacle += 1
                solution(i, j)
                graph[i][j] = 'X'
                obstacle -= 1
solution(0, 0)
print(result) # 계산하기