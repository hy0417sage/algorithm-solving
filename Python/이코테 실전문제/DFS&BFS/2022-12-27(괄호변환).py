# 소스 코드 내 괄호가 개수는 맞지만 짝이 맞지 않음
# 소스코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려준다.
# () 개수가 같다면 -> 균형잡힌 문자열
    # 1. 균형잡힌 문자열 나누는 함수 만들기 u, v
# () 짝이 모두 맞을 경우 -> 올바른 문자열
    # 2. 올바른 문자열 확인 함수 만들기

# 올바른 문자열 확인 3, 4번
def checkCorrect(u):
    stack = []
    for s in u:
        if s == '(':
            stack.append(s)
        if s == ')':
            if len(stack) <= 0:
                return False
            stack.pop()

    return True

# 군형잡힌 문자열 분리(u, v로 분리)
def balanceDiv(char):
    left, right = 0, 0
    for c in range(len(char)):
        if char[c] == '(':
            left += 1
        if char[c] == ')':
            right += 1
        if left == right:
            return char[:c+1], char[c+1:]


def solution(p):
    answer = ''

    #1
    if p == '':
        return ''
    #2
    u, v = balanceDiv(p)

    #3
    if checkCorrect(u):
        return u + solution(v)

    #4
    else:
        answer = '(' #1
        answer += solution(v) #2 이어 붙인다.
        answer += ')' #3 다시 붙인다.
        u, resultU = u[1:-1], ''

        for i in u:
            if i == '(':
                resultU += ')'
            if i == ')':
                resultU += '('

        answer += resultU #4 u의 첫번째 마지막 문자열 제거, u의 나머지 괄호 방향 뒤집고 붙이기

    return answer