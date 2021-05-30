N, K = map(int, input().split())

AB = [] * N

for i in range(N):
  AB.append(list(map(int, input().split())))

AB.sort(key=lambda x: x[0])

money = K

for p in AB:
  if(p[0]<=money):
    money += p[1]
  else:
    break

print(money)
