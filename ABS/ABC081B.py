N = int(input())
A = list(map(int, input().split()))

cnt = 0

while True:
  if (len(list(filter(lambda x:x%2!=0, A))) > 0):
    break
  else:
    A = list(map(lambda x:x//2, A))
    cnt += 1

print(cnt)
