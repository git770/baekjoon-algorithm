# Map(딕셔너리) 구조를 이용한 알고리즘
d = dict()

for _ in range(int(input())) :
    book = input()
    if book in d :
        d[book] += 1
    else :
        d[book] = 1
     
# 딕셔너리에서 제공하는 메소드       
#d.keys() 키값만 모아서 반환
#d.items() 키, value 모아서 반환
#d.values()  값을 모아서 반환

m = max(d.values()) # value에서 가장 많이 저장된 값
candi = [] # 가장 많이 팔린 책 후보들
for k, v in d.items() :
    if v == m :
        candi.append(k)

candi.sort() # 후보들 정렬
print(candi[0]) # 정렬 후 가장 앞에 있는 값 책 출력 