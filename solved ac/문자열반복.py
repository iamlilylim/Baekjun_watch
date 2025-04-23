t = int(input())
for _ in range(t):
    a, b = input().split()
    a = int(a)
    result = ""
    for let in b:
        result +=let*a

    print(result)