t = int(input())



for i in range(t):
    an = list(input())
    count = 1
    for j,ch in enumerate(an):
        if ch == 'O':
            an[j] = str(count)
        count += 1


    print(ch)