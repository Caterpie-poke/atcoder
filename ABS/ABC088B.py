N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

Alice = sum([a[i] for i in range(0,N,2)])
Bob = sum([a[i] for i in range(1,N,2)])

print(Alice - Bob)
