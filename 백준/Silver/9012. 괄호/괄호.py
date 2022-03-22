T = int(input())

for _ in range(T) :
   stk = [] #파이썬에서는 stack은 그냥 리스트로 사용하면 됨
   isVPS = True
   for ch in input() :
        if ch == '(':
            stk.append(ch)
        else:
            if len(stk) > 0:
                stk.pop()
            else :
                isVPS = False    
                break
    
   if len(stk) > 0:
        isVPS = False

   print('YES' if isVPS else 'NO')