t = int(input())
for _ in range(t):
    count = 1
    b = list(input())
    for j in range(len(b)):
        if b[j] == 'O':
            b[j] = count
            count += 1

        else:
            b[j] = '0'

    print(sum(map(int,b)))