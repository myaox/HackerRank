d = {}
for _ in range(int(input())):
    l = input().split()
    d[l[0]] = list(map(float,l[1:]))
t = d[input()]
print("{:.2f}".format(sum(t) / len(t)))

