N, M = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(M) ]

dp = [[10**9] * (2**N) for _ in range(M+1)]

dp[0][0] = 0
for i in range(M):
    discount_idx = 0
    for j in range(N):
        if A[i][j]:
            discount_idx += 2**j

    for j in range(2**N):
        if dp[i][j] < 10**9:
            # i番目のクーポンを使う
            dp[i+1][j|discount_idx] = min(dp[i+1][j|discount_idx], dp[i][j]+1)

            # i番目のクーポンを使わない
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])

ans = dp[M][2**N-1]
if ans < 10**9:
    print(ans)
else:
    print(-1)




