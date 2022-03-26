N, L = map(int, input().split()) # N : 물이 새는 곳의 개수
                                 # L : 테이프 길이
coord = [False] * 1001           # 모든 위치에 False로 초기화                     
for i in map(int, input().split()) : # 물이 새는 곳의 위치에 True로 변경
    coord[i] =  True

ans = 0    # 사용한 테이프의 개수
x = 0 # 현재 살펴보고 있는 좌표
while x < 1001 :    
    if coord[x] :   # 물이 새는 곳을 확인하면,
        ans += 1    # 테이프를 하나 사용
        x += L      # 테이프의 길이(L) 만큼 그 다음 좌표에서 물이 새는 유무와 상관없이 사용되기 때문에, x좌표는 테이프의 길이만큼 점프 
                     
    else : 
        x += 1  # 물이 새지 않는다면 x좌표를 1씩 증가해 다음 좌표 확인
print(ans)
