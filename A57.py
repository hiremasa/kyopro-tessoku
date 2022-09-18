N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 前計算
dp = [[0] * N for _ in range(30)]
for i in range(N):
    dp[0][i] = A[i] - 1

for i in range(1, 30):
    for j in range(N):
        dp[i][j] = dp[i-1][dp[i-1][j]]

for _ in range(Q):
    x, y = map(int, input().split())

    current_place = x - 1

    for d in range(30)[::-1]:
        if (y >> d) & 1: # (Y // (2 ** d)) % 2 のこと
            current_place = dp[d][current_place]

    print(current_place + 1)


