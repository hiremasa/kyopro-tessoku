class point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

N = int(input())
points = [None] * N
for i in range(N):
    x, y = map(int, input().split())
    points[i] = point2d(x, y)

# 貪欲法
current_place = 0
visited = [0] * N
visited[0] = True
P = [ 0 ]

for i in range(1, N):
    min_dist = 10**10
    min_idx = -1 # つぎどこに行くか
    for j in range(N):
        cur_dist = points[current_place].dist(points[j])
        if not visited[j] and cur_dist < min_dist:
            min_dist = cur_dist
            min_idx = j

    visited[min_idx] = 1
    P.append(min_idx)
    current_place = j
P.append(0)

for i in P:
    print(i + 1)

