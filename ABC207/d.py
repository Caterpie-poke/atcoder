N = int(input())

KUKAN = [] * N

for i in range(N):
  a,b = list(map(int, input().split()))
  if   (t == 1):
    KUKAN.append((l,r))
  elif (t == 2):
    KUKAN.append((l,r-0.1))
  elif (t == 3):
    KUKAN.append((l+0.1,r))
  elif (t == 4):
    KUKAN.append((l+0.1,r-0.1))
  else:
    pass

for i in range(N):
  c,d = list(map(int, input().split()))


ans = 0

for i in range(N-1):
  for j in range(i+1, N):
    il,ir = KUKAN[i]
    jl,jr = KUKAN[j]
    has_same_part = not( ir < jl or jr < il )
    if(has_same_part):
      ans += 1


print(ans)
