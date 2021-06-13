N, M = map(int, input().split())

town = [-1] * (N+1)

def get_depth(arr, start, dest, d, passed):
  if(dest != -1 and dest != start and dest not in passed):
    passed.append(dest)
    return get_depth(arr, start, arr[dest], d+1, passed)
  else:
    return d

for i in range(M):
  A,B = map(int, input().split())
  town[A] = B

for i in range(N+1):
  town[i] = i

cnt = 0
for i in range(1, N+1):
  cnt += get_depth(town, i, town[i], 0, [])


print(cnt)
