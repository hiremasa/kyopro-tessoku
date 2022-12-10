H, W = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(H)]
from itertools import accumulate


A = [[None] for _ in range(W)]
for w, x in enumerate(zip(*X)):
    A[w] = list(accumulate(x))
B = [[None] for _ in range(H)]
for h, x in enumerate(zip(*A)):
    B[h] = list(accumulate(x))

C = [[0] * (W+1) for _ in range(H+1)]
for h in range(H):
    C[h+1][1:] = B[h]

#for h in range(H+1):
#    print(C[h])
Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
#    print(C[c][d] , C[a-1][b-1] , C[a-1][d] , C[c][b-1])
    ans = C[c][d] + C[a-1][b-1] - C[a-1][d] - C[c][b-1]
    print(ans)


