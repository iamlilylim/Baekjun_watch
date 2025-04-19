'''

2 T
6 12 10 H, W, N -> 402
30, 50, 72 H, W, N -> 1203


'''

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    width = n // h +1 #호수는 몫+1
    hi = n%h #층수는 나머지
    if n%h==0:
        width = n//h
        hi = h

    print(hi*100 + width)

