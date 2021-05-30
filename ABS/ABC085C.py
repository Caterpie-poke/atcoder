N, Y = map(int, input().split())

ans = [-1,-1,-1]

try:
  for x in range(N, -1, -1):
    if(10000*x > Y): continue
    if(5000*(N-x) < Y-10000*x): raise Exception
    for y in range(N-x, -1, -1):
      if(10000*x + 5000*y > Y): continue
      if(1000*(N-x-y) < Y-10000*x-5000*y): raise Exception
      for z in range(N-x-y, -1, -1):
        culc = 10000 * x + 5000 * y + 1000 * z
        if (culc == Y and x+y+z == N):
          ans = [x,y,z]
          raise Exception
except Exception:
  pass

print(f"{ans[0]} {ans[1]} {ans[2]}")
