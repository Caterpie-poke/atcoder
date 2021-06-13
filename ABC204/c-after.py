'''
アライグマ「ABC204のwriterだったのだ！　C問題はBFSやDFSをN回やるのだ！　昨日の典型で似たような問題が出てちょっとびっくりしたのだ」
'''

'''
幅優先探索：BFS (Breadth First Search)
深さ優先探索：DFS (Depth First Search)
グラフの探索方法、ノードから近いノードを順に探索していく
スタックまたはキューを用いる（BFS→キュー、DFS→スタック）
'''


N, M = map(int, input().split())

route = [[False] * (N+1)] * (N+1)


def cp(arr1, arr2):
  updated = False
  for i in range(len(arr1)):
    if(arr1[i]):
      arr2[i] = True
      updated = True
  return updated


for i in range(M):
  A,B = map(int, input().split())
  route[A][B] = True

for i in range(1, N+1):
  route[i][i] = True

print('====================')
print(route)
print('====================')

updated = True
for epoch in range(N):
  if(not updated):break
  for i in range(1,N+1):
    if(i < N and ):
      updated = cp(route[i+1],route[i])
    else:
      updated = cp(route[0], route[i])

print('====================')
print(route)
print('====================')


cnt = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    cnt += 1 if route[i][j] else 0


print(cnt)
