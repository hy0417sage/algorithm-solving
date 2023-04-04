# 첫번쨰 문제
n, m = map(int, input().split())
tukk = list(map(int, input().split()))

tukk.sort()


def binary_search(target, start, end, sum_tukk, len_tukk):
  while start <= end:
    mid = (start + end) // 2
    tukk_check = sum_tukk - (len_tukk * mid)
    print('check0', tukk_check)
    if tukk_check == target: #요청한 길이와 계산한 길이가 맞으면..
      print('check1', mid)
      return mid
    elif tukk_check < target:
      print('check2', start, mid, end)
      end = mid - 1
    else:
      print('check3', start, mid, end)
      start = mid + 1

print(binary_search(m, 0, max(tukk), sum(tukk), len(tukk)))