# (1)이진 탐색
# (2)계수 정렬
# (3)집합 자료형 으로 풀 수 있다.
# 나는 이진 탐색을 만들어 풀었지만, 파이썬의 in을 사용하여 푸는 것이 코드를 줄이는데 효과적일 것같아 다시 풀었다.
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')