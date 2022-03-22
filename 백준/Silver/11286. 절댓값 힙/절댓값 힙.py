import heapq
import sys

#input을 빠르게 출력
input = sys.stdin.readline 
n = int(input())
pq = []

for i in range(n) :
    inputV = int(input())
    if inputV != 0 :
        heapq.heappush(pq, (abs(inputV), inputV))
    else :
        if pq:
            print(heapq.heappop(pq)[1])
        else : 
            print(0)