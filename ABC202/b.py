S = input()
l = list(S)
l.reverse()
d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

print(''.join(list(map(lambda x: d[x], l))))
