A,B,C,D = list(map(int, input().split()))

mizu = A
aka = 0
epoch = 0

if(C * D <= B):
  print(-1)
else:
  while True:
    if(mizu <= aka * D):
      break
    mizu += B
    aka += C
    epoch += 1
  print(epoch)

