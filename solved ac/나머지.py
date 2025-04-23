num = []
for _ in range(10):
    n = int(input())
    num.append(n)
x = []
for d in num:
    x.append(d%42)

print(len(set(x)))