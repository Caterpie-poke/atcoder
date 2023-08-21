N,A,X,Y = map(int, input().split())

if (N > A):
  print((N-A)*Y + A * X)
else:
  print(X * N)
