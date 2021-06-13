from collections import Counter

N, M = map(int, input().split())

root = {}

for x in range(N+1):
  root[x] = {x: True}

for i in range(M):
  A,B = map(int, input().split())
  if(B in root):
    root[B][A] = True
  else:
    root[B] = {A: True}
  if(A in root):
    for k in root[A].keys():
      root[B][k] = True

root[0][0] = False

cnt = 0
for x in root.keys():
  for y in root[x].keys():
    if root[x][y]:
      cnt += 1
      print(f"({y},{x})")


print(cnt)
