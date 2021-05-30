N, K = map(int, input().split())

total = 0
for i in range(1,N+1):
  for j in range(1,K+1):
    total += 100+j+(i-1)*100

print(total)
