// 중복 지우기
리스트.distinct()

// count 같은 값(숫자 등) 갯수 구하기
resultArr.filter{it == i}.count()

// 두번째 숫자를 기준으로 리스트를 큰수대로 정렬 / map -> list -> map 형변환
answerMap.toList().sortedBy { it.second }.reversed().toMap()