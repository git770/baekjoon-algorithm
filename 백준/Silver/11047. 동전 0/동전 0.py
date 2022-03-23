#문제에서 배수라는 말이 나왔고 그리디임을 예상
#배수라는 말이 안나왔으면 반례가 있었을 수도 있어 그리디로 못했을 것

#처리사항
# 1. 동전의 총 종류(N), 동전이 합쳐져서 얼마가 되어야 하는지(k) 입력
# 2. N개의 수만큼 동전을 오름차순으로 입력
# 3. k원을 만드는데 필요한 동전 개수의 최솟값 출력

n, k = map(int,input().split())

coinLst = [int(input()) for _ in range(n)] # 바로 초기화 
coinLst.reverse()                          # 동전 개수의 최솟값을 출력해야 하므로 동전 단위가 제일 큰 것 부터 계산해야 하며, 
                                           # coinLst를 역순으로 변경해준다.
                                          
ans = 0

for coin in coinLst :
    ans += k // coin # k를 coin 으로 나눈 몫 (동전 개수의 최소값을 저장하기 위해)
    k %= coin # k를 coin으로 나눈 나머지 값 (coin으로 나눈 나머지 값을 통해 남은 값 계산)
    
print(ans)    