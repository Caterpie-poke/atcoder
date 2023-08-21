import copy

N,K = map(int, input().split())

a = list(map(int, input().split()))

aa = copy.deepcopy(a)
a.sort()

sames = K // N
lucky = K % N

for n in aa:
  if(a.index(n) < lucky):
    print(sames + 1)
  else:
    print(sames)

