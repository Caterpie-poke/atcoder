P = int(input())

KAIJOU = []

for i in range(1, 11):
  if (i == 1):
    KAIJOU.append(i)
  else:
    KAIJOU.append(i * KAIJOU[i-2])

KAIJOU.sort(reverse=True)

amt = P
cnt = 0
pmax = KAIJOU.pop(0)
while amt > 0:
  if(pmax <= amt):
    cnt += 1
    amt -= pmax
  else:
    pmax = KAIJOU.pop(0)


print(cnt)
