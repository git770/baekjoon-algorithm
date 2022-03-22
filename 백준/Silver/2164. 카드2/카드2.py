from collections import deque
n = int(input())
dq = deque()
#dq = deque(range(1, n+1)) //아래의 for문을 쓰지 않고 바로 이렇게 쓸 수 있음


for i in range(1, n+1) :
   dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())