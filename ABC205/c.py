A, B, C = map(int, input().split())

ans = ''

if(C % 2 == 0):
  if(abs(A) == abs(B)):
    ans = '='
  elif(abs(A) < abs(B)):
    ans = '<'
  elif(abs(A) > abs(B)):
    ans = '>'
  else:
    ans = 'Unknown'
else:
  if(A == B):
    ans = '='
  elif(A < B):
    ans = '<'
  elif(A > B):
    ans = '>'
  else:
    ans = 'Unknown'

print(ans)
