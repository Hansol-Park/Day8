#Day 8
#I think Day 7 is null.
#Hmm..

#081 별 표현식
#기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다.
#하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다.
#튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.

a,b,*c = (0,1,2,3,4,5)
print(a)
print(b)
print(c)

#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(scores)
*valid_score, _, _=scores
print(valid_score)
print(_)

#082
#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_, _, *valid_score = scores
print(valid_score)

#083
#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.

_,*valid_score,_ = scores
print(valid_score)

#084 비어있는 딕셔너리
#temp 이름의 비어있는 딕셔너리를 만들라.

temp = {}
print(temp)

#085
#다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.

ice = {"메로나": 1000,"폴라포": 2000,"빵빠레": 3000}
print(ice)

#086
#085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.

ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

#087
#다음 딕셔너리를 사용하여 메로나 가격을 출력하라.

icecream = input()
print(icecream,"가격 :",ice[icecream])

#CODEUP에서 배운 INPUT 사용 결과.
#INPUT 사용해서 아이스크림 검색 후 결과 출력 가능.
#엄청난 발전!! Feel So good..

#088
#다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.

ice["메로나"] = 1300
print(ice)

#089
#다음 딕셔너리에서 메로나를 삭제하라.

del ice["메로나"]
print(ice)

#090
#다음 코드에서 에러가 발생한 원인을 설명하라.

#>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#>> icecream['누가바']
#Traceback (most recent call last):
# File "<pyshell#69>", line 1, in <module>
#    icecream['누가바']
#KeyError: '누가바'

#Dict 내부에 있는 아이스크림아 아니기 때문에 출력 불가능.