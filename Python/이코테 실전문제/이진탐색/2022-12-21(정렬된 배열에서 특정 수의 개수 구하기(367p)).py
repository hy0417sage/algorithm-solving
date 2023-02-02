n, x = map(int, input().split())
num_list = list(map(str, input().split()))

result = num_list.count(str(x))

if result == 0:
  print(-1)
else:
  print(result)