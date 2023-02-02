# 자연수를 3진법 상에서 앞뒤로 뒤집는다. 
# 이를 다시 10진법으로 표현한다.
def conversion(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3) # 3진법
        rev_base += str(mod)
    return rev_base

def solution(n):
    answer = list(str(conversion(n)))
    answer = ''.join(answer)
    return int(str(answer), 3)