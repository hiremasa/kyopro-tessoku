D = int(input())
N = int(input())

import itertools
Attend = [0] * (D + 2)

for _ in range(N):
    l, r = map(int, input().split())
    Attend[l] += 1
    Attend[r + 1] += -1

Attend = list(itertools.accumulate(Attend))
for i in range(D):
    print(Attend[i+1])
