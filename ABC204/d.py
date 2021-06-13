'''
アライグマ「D問題はDPなのだ！　料理を2つに分けて合計時間の大きい方が小さくなるようにすればいいから「いくつか選んで和をsum/2以上にするときの最小値」が求まれば良くて、部分和問題だからDPすれば解けるのだ！」
'''

N = int(input())
T = list(map(int, input().split()))

T.sort()

def get_ans(arr):
  if(len(arr) > 2):
    l = arr[-1]
    r = arr[-2]
    rest = get_ans(arr[0:-2])
    adder = min(l,r)
    print(f"{adder} + {rest}")
    return adder + rest
  elif(len(arr) == 2):
    return max(arr[0], arr[1])
  elif(len(arr) == 1):
    return arr[0]
  elif(len(arr) == 0):
    return 0
  else:
    raise Exception("わかめ")

print(get_ans(T))


