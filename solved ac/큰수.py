nu = []
for _ in range(9):
    num = int(input())
    nu.append(num)
a = max(nu)
print(a)
print(nu.index(a)+1)
