import sys

S = input()
L = len(S)
KEYWORD = 'chokudai'

sys.setrecursionlimit(10**9+7)

memo = {
  "chokudai" : [-1]*L,
  "hokudai" : [-1]*L,
  "okudai" : [-1]*L,
  "kudai" : [-1]*L,
  "udai" : [-1]*L,
  "dai" : [-1]*L,
  "ai" : [-1]*L,
  "i" : [-1]*L
}


def cnt_chokudai(s, tgt):
  rest = len(s)-1
  if(len(s) < len(tgt)):
    return 0
  else:
    # sの先頭が探す文字列の先頭の場合、sの先頭を消費するケースを考慮する
    if(s[0] == tgt[0]):
      # 検索対象が1文字なら消費して終了
      if(len(tgt) == 1):
        use = 1
      else:
        # 残り部分を探索済みの場合
        if(memo[tgt[1:]][rest] != -1):
          use = memo[tgt[1:]][rest]
        # まだの場合
        else:
          use = cnt_chokudai(s[1:], tgt[1:])
          memo[tgt[1:]][rest] = use
    else:
      use = 0

    # sの先頭を消費しない場合
    # 残り部分を探索済みの場合
    if(memo[tgt][rest] != -1):
      not_use = memo[tgt][rest]
    # まだの場合
    else:
      not_use = cnt_chokudai(s[1:], tgt)
      memo[tgt][rest] = not_use

    return (use % ((10**9) + 7) + not_use % ((10**9) + 7)) % ((10**9) + 7)


print(cnt_chokudai(S, KEYWORD))


