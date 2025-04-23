while 1:
    try:
        a, b = map(int, input().split())
        print(a + b)
    finally:
        a==0, b==0
        break
