from operator import itemgetter
l = sorted([[input(), float(input())]for _ in range(int(input()))],key=itemgetter(0))
n = sorted(set(x[1] for x in l))[1]
print(*list(x[0] for x in l if x[1] == n), sep="\n")
