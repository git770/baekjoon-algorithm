N = int(input()) #지방의 수
req = list(map(int, input().split())) # 요청 금액
M = int(input()) # 총 예산

lo = 0 # 가장 낮은 
hi = max(req) # 요청 금액 중 최대
mid = (lo + hi) // 2 # 중간 값
ans = 0 

# 상한선 파라미터를 받고, 지방마다 얼마를 줄 지, 총 예산(M) 이하인지 이상인지 확인
def is_possible(mid):
    return sum(min(r, mid) for r in req) <= M # 총 합이 M이하면 true 이상이면 false 반환

# 이분탐색    
while lo <= hi:
    if is_possible(mid): 
        lo = mid + 1 # mid를 is_possible에서 탐색했기에 mid + 1
        ans = mid
    else:
        hi = mid - 1 # 상한선을 낮춘다
    
    mid = (lo + hi) // 2  # mid 갱신       

print(ans)