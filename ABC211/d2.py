N, Q = map(int, input().split())
A = list(map(int, input().split()))


def get_ans(n, skip):
  if(n in A):
    if(skip == -1):
      skip = len(list(filter(lambda x: x < n, A)))
    return get_ans(n+1, skip)
  elif(skip > 0):
    return get_ans(n+1, skip-1)
  else:
    return n


ans = []

for i in range(Q):
  k = int(input())
  ans.append(get_ans(k, -1))

for a in ans:
  print(a)
