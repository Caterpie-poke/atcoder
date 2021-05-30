N = int(input())

d = [] * N
for i in range(N):
  d.append(int(input()))

print(len(set(d)))
