MOD = 10007

# 초기값 설정
dp = [0] * 1001
dp[1] = 1 
dp[2] = 2 

n = int(input())
for i in range(3, 1001): # 1000보다 크거나 같은 직사각형이므로 1001까지 반복
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[n])