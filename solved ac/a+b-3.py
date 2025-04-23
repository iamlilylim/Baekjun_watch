t = int(input())

for _ in range(t):
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
