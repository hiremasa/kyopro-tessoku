import random

class point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

def get_score(N, point, P):
    score = 0
    for i in range(N):
        score += point[P[i]].dist(point[P[i+1]])
    return score

# input
N = int(input())
point = [None] * N
for i in range(N):
    x, y = map(int, input().split())
    point[i] = point2d(x, y)

# 山登り法

# 初期解
P = [ i % N for i in range(N + 1) ]
current_score = get_score(N, point, P)

NUM_LOOPS = 40000
for _ in range(NUM_LOOPS):
    #  反転させる区間 [L, R] を選ぶ
    l = random.randint(1, N-1) # 1 以上 n-1 以下のランダムな整数
    r = random.randint(1, N-1)
    if l > r:
        l, r = r, l
    # P[l], P[l+1], ..., P[r] を逆順にする
    P[l:r+1] = P[l:r+1][::-1]
    new_score = get_score(N, point, P)

    if new_score < current_score:
        current_score = new_score
    else:
        P[l:r+1] = P[l:r+1][::-1]

for p in P:
    print(p + 1)

