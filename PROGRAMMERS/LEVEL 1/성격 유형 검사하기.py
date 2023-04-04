def solution(survey, choices):
    answer = [3, 2, 1, 0, 1, 2, 3]
    personalities = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    result = ""

    # 각 유형별 크기 계산
    for s, c in zip(survey, choices):
        left, right = s[0], s[1]
        if c < 4:
            personalities[left] += answer[c - 1]
        else:
            personalities[right] += answer[c - 1]

    # 어느 유형인지 결과 계산
    personalities = list(personalities.items())

    for i in range(0, len(personalities) - 1, 2):
        if personalities[i][1] >= personalities[i+1][1]:
            result += personalities[i][0]
        else:
            result += personalities[i+1][0]

    return result