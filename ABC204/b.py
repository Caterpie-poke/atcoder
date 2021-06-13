N = int(input())
A = map(int, input().split())

ans = sum(list(map(lambda x: x - 10, filter(lambda x: x > 10, A))))

print(ans)
