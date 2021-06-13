N, Q = map(int, input().split())
A = list(map(int, input().split()))

K = [0] * Q
for i in range(Q):
  K[i] = int(input())

MAX_K = max(K)

all_list = list(range(1, MAX_K + N + 1))

ans = sorted(list(set(all_list) - set(A)))


for k in K:
  print(ans[k-1])
