# 1. 게시판 불량 이용자 신고 
    # 1) 한번에 한명만 신고 가능
    # 2) 동일한 유저 신고 횟수는 1회로 처리
# 2. 처리결과 메일로 발송
    # K번 이상 신고된 유저는 게시판 이용 정지
    # 신고한 모든 유저에게 메일로 발송 
from collections import defaultdict

def solution(id_list, report, k):
    
    report = set(report) #중복제거
    emails = defaultdict(list) # 딕셔너리 초기화
    result = defaultdict(int)
    
    for id in id_list:
        result[id] = 0
    
    for r in report:
        reporter, reported = r.split(" ")
        emails[reported].append(reporter)
        
    # K번 이상 신고 당했는지 확인
    for key, reporterList in emails.items():
        # 신고당한 자가 K번 이상의 신고 횟수를 가지고 있을 경우
        if len(reporterList) >= k: 
            # 신고한 reporter에게 email를 보내줘야 함
            for reporter in reporterList:
                if reporter in id_list:
                    result[reporter] += 1

    return list(result.values())


### 같은 아이디어로 푼 다른 사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID

    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer