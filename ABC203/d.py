import statistics

N, K = map(int, input().split())

A = []

for i in range(N):
  A.append(list(map(int, input().split())))

L = 0
if(N==K):
  L = 1
elif(N%K==0):
  L = N//K
else:
  L = N//K + 1

centers = [] * L**2

# どう見てもTLEなコード
for i in range(0,N-K+1):
  for j in range(0,N-K+1):
    tmp = []
    for ii in range(K):
      for jj in range(K):
        tmp.append(A[i+ii][j+jj])
    centers.append(statistics.median_low(tmp))

print(min(centers))

