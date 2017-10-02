_, n = map(int, input().split(" "))
l = []
for i in range(n):
    l.append(list(map(float,input().split(" "))))

for nums in zip(*l):
    print(sum(nums)/ len(nums))
