while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError: #EOFError가 뜨면
        break   #멈춰라