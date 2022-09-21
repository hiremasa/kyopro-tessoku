# seg tree 0-index
class segtree:
    # 要素datの初期化を行う 最初は全部0
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2

        self.dat = [0] * (self.size * 2)

    def update(self, pos, x):
        # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
        pos = pos + self.size

        self.dat[pos] = x

        while pos >= 2:
            pos //= 2
            self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])

    # u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r)
    # は求めたい半開区間
    def query(self, l, r, a, b, u):
        if r <= a or b <= l:
            return -float("inf") # 一切含まれない場合

        if l <= a and b <= r:
            return self.dat[u]

        m = (a + b) // 2
        answerl = self.query(l, r, a, m, 2 * u)
        answerr = self.query(l, r, m, b, 2 * u + 1)
        return max(answerl, answerr)

# 入力
N, Q = map(int, input().split())

# クエリの処理
Z = segtree(N)
for _ in range(Q):
    tp, *cont = map(int, input().split())

    if tp == 1:
        pos, x = cont
        Z.update(pos - 1, x)
    elif tp == 2:
        l, r = cont
        ans = Z.query(l-1, r-1, 0, Z.size, 1)
        print(ans)
