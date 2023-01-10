# 나의 풀이
def solution(n, arr1, arr2):
    answer = []
    answer1, answer2 = [], []
    
    for i in range(n):
        answer1.append(format(arr1[i], 'b').zfill(n))
        answer2.append(format(arr2[i], 'b').zfill(n))
    
    for i in range(n):
        tmp = ''
        for a1, a2 in zip(answer1[i], answer2[i]):
            if a1 == '0' and a2 == '0':
                tmp += ' '
            elif a1 == '1' or a2 == '1':
                tmp += '#'
        answer.append(tmp)
                      
    return answer

# 다른사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer