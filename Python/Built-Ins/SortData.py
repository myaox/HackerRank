n, m = map(int, input().split(" "))
l = []
for _ in range(n):
    l.append(list(map(int, input().split(" "))))

for ls in sorted(l,key=lambda x:x[int(input())]):
    print(*ls)
