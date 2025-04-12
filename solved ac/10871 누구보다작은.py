#n, x = input().split()
#n = int(n)
##x = int(x)
#a = list(input(map.range(n)))
#for i in a:
#    print()

n, x = map(int, input().split())
numbers = list(map(int,input().split()))

for i in range(n):
    if numbers[i] < x:
        #print(numbers[i], end=' ')
        print(i, end=' ')