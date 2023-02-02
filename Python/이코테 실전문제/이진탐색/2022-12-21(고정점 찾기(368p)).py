n = int(input())   #N 개의 서로 다른 원소
list_a = list(map(int, input().split())) # 수열

def binary_search(array, start, end):
  if start > end:
    print(-1)
    return None
  mid = (start + end) // 2
  if array[mid] == mid:
    print(mid)
    return mid
  elif array[mid] > mid:
    binary_search(array, start, mid - 1)
  else:
    binary_search(array, mid + 1, end)

binary_search(list_a, 0, n-1)