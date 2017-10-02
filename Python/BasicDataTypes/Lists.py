l = []
for _ in range(int(input())):
    args = input().split(" ")
    if args[0] == "print":
        print(l)
    else:
        eval("l." + args[0] + "(" + ",".join(args[1:]) + ")")
