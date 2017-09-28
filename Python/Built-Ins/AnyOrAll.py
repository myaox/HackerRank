_, l = input(), input().split(" ")
print(all(list(map(lambda x: int(x) > 0 ,l))) and any(list(map(lambda x: x == x[::-1], l))))
