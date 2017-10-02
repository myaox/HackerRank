def f(s):
    try:
        n = int(s)
        if n % 2 == 0:
            n = "zz" + str(n)
        else:
            n = "z" + str(n)
        return n
    except:
        return s.swapcase()

print(*sorted(input(), key=f), sep="")
