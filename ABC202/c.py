N = int(input())

A = [0] * N
A = list(map(int, input().split()))
B = [0] * N
B = list(map(int, input().split()))
C = [0] * N
C = list(map(int, input().split()))


memo = [-1] * (N+1)
cnt = 0
for i in range(N):
  if (memo[A[i]] == -1):
    memo[A[i]] = 0
    for j in range(N):
      if(A[i] == B[C[j] - 1]): memo[A[i]] += 1
  cnt += memo[A[i]]

print(cnt)



