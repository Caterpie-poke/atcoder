N,A,B = map(int, input().split())

total = 0

for i in range(N):
  n = str(i+1)
  ketasum = sum(list(map(int, n)))
  if(A <= ketasum and ketasum <= B):
    total += int(n)

print(total)
