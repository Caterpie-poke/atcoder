N = int(input())
A = list(map(int, input().split()))

B = list(range(1,N+1))
A.sort()

if(A==B):
  print('Yes')
else:
  print('No')
