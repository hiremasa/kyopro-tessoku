N, Q = map(int, input().split())
A = list(map(int, input().split()))
import itertools
A_acc = [0] + list(itertools.accumulate(A))

for _ in range(Q):
    l, r = map(int, input().split())
    print(A_acc[r] - A_acc[l-1])
