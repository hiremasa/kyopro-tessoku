N, Q = map(int, input().split())
S = input()

B = 100
mod = 2147483647

# 文字を数値に変換
# ord(c) で文字 c の文字コード（ASCII コード）を取得
T = list(map(lambda c: ord(c) - ord("a") + 1, S))

# 100のn乗を前計算する
power100 = [None] * (N+1)
power100[0] = 1
for i in range(N):
    power100[i+1] = power100[i] * 100 % mod

H = [0] * (N + 1)
for i in range(N):
    H[i+1] = (100 * H[i] + T[i]) % mod

def hash_value(l, r):
    return (H[r] - H[l-1] * power100[r-l+1]) % mod

for _ in range(Q):
    a, b, c, d = map(int, input().split())

    hash_l = hash_value(a, b)
    hash_r = hash_value(c, d)

    print("Yes" if hash_l == hash_r else "No")


