# 처리사항

# 1. 난쟁이들의 키 입력
# 2. 입력한 값들의 합을 구하기 위해 7명의 난쟁이들의 키를 뽑는다.
# 3. 7명의 난쟁이들의 키의 합은 100이여야 한다.
# 4. 총 합이 100인 키들의 조합을 오름차순으로 정렬한다.
# 5. 키의 합이 100이 된 조합을 찾으면 더 이상 실행하지 못하도록 
#    break 처리 해준다. 

from itertools import combinations

heights = []
for _ in range(9) :
    heights.append(int(input()))

for combi in combinations(heights, 7):
        if sum(combi) == 100 : 
            for height in sorted(combi) :
                print(height)
            break                       # break 처리 중요!